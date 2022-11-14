# -*- coding: utf-8 -*-
"""
@Authors Kilian Raude, Colin Pelletier, Joris Monnet


Helper class
"""

import numpy as np
import csv


def remove_constant_features(tx):
    """Remove features with a std = 0"""
    vars = np.nanvar(tx, axis=0)
    constant_ind = np.where(np.isclose(vars, 0))[0]
    return np.delete(tx, constant_ind, axis=1)


def get_split_by_jet_data(y, tx, jet, jet_column=18):
    """Get y and tx where PRI_jet_num value = a specified jet number"""
    indices = np.where(tx[:, jet_column] == jet)
    return y[indices], tx[indices]


def robust_scaling(tx, q1, q2, q3, jet_column=17):
    """Robust scaling -> remove median and divide by iqr for every columns but PRI_jet_num"""
    res = (tx - q2) / (q3 - q1)
    res[:, jet_column] = tx[:, jet_column]
    return res


def remove_outliers(tx, q1, q3):
    """
    Use IQR method from https://online.stat.psu.edu/stat200/lesson/3/3.2
    to remove outliers
    """
    iqr = q3 - q1
    outq1 = np.where(tx < q1 - 1.5 * iqr)
    outq3 = np.where(tx > q3 + 1.5 * iqr)
    tx[outq1] = np.take(q1 - 1.5 * iqr, outq1[1])
    tx[outq3] = np.take(q3 + 1.5 * iqr, outq3[1])
    return tx


def transform(tx, IDs_degrees):
    """Remove constants, handle degrees, remove outliers, and standardize with robust scaling"""
    tx = remove_constant_features(tx)
    tx = expand_degrees(tx, IDs_degrees)

    q1 = np.nanpercentile(tx, q=25, axis=0)
    q2 = np.nanpercentile(tx, q=50, axis=0)
    q3 = np.nanpercentile(tx, q=75, axis=0)

    tx = remove_outliers(tx, q1, q3)

    return robust_scaling(tx, q1, q2, q3)


def replace_nan_by_means(data, mean_data=None):
    """
    mean_dataset : use it if the value has already been computed
        array of shape (D) (contains the mean of each feature column)

    Test :  arr_test = np.array([[1, 2, 3, 4], [10, np.nan, 11, 12], [np.nan, 13, 14, np.nan], [np.nan, 15, 16, 17]])
            arr_test_theoric = replace_nan_by_means(arr_test)
            assert(np.allclose(arr_test_theoric[1, 1], np.nanmean(arr_test[:, 1]))) #, "mean not computed correctly"
    """

    for col_idx in range(data.shape[1]):
        dataset_col = data[:, col_idx]
        dataset_col[np.isnan(dataset_col)] = mean_data[col_idx]

    return data


def expand_degree(x, ID_feature):
    """Replace each degree feature by a feature of its sine and one of its cosine"""
    x = np.c_[x, np.cos(x[:, ID_feature])]
    x[:, ID_feature] = np.sin(x[:, ID_feature])
    return x


def expand_degrees(x, IDs_Features):
    """Expand degrees for each features using degrees as unit"""
    for ids in IDs_Features:
        x = expand_degree(x, ids)
    return x


def load_csv_data(data_path, sub_sample=False):
    """Loads data and returns y (class labels), tX (features) and ids (event ids)"""
    y = np.genfromtxt(data_path, delimiter=",", skip_header=1, dtype=str, usecols=1)
    x = np.genfromtxt(data_path, delimiter=",", skip_header=1)
    ids = x[:, 0].astype(np.int)
    input_data = x[:, 2:]

    # convert class labels from strings to binary (-1,1)
    yb = np.ones(len(y))
    yb[np.where(y == "b")] = -1

    # sub-sample
    if sub_sample:
        yb = yb[::50]
        input_data = input_data[::50]
        ids = ids[::50]

    return yb, input_data, ids


def create_csv_submission(ids, y_pred, name):
    """
    Creates an output file in .csv format for submission to Kaggle or AIcrowd
    Arguments: ids (event ids associated with each prediction)
               y_pred (predicted class labels)
               name (string name of .csv output file to be created)
    """
    with open(name, "w") as csvfile:
        fieldnames = ["Id", "Prediction"]
        writer = csv.DictWriter(csvfile, delimiter=",", fieldnames=fieldnames)
        writer.writeheader()
        for r1, r2 in zip(ids, y_pred):
            writer.writerow({"Id": int(r1), "Prediction": int(r2)})


def get_col_idx(col_name, col_names):
    """
    Get col index given the feature name (for the initial features only)
    """
    return [col_idx - 2 for col_idx, name in enumerate(col_names) if col_name == name][
        0
    ]


def log_transform(x_tr, x_te, cols_idx):
    """
    Change some column for their log to minimize impact of some big values
    """
    for col_idx in cols_idx:
        x_tr[:, col_idx] = np.log(x_tr[:, col_idx] + 1)  # +1 to avoid log(0)
        x_te[:, col_idx] = np.log(x_te[:, col_idx] + 1)

    return x_tr, x_te


def remove_nan_columns(x, max_nan_ratio=0.5):
    """
    Remove columns with more than a ratio of NaN values
    """
    nb_nan = np.count_nonzero(np.isnan(x), axis=0)
    nan_ratio = nb_nan / x.shape[0]

    x = x[:, nan_ratio <= max_nan_ratio]
    return x
