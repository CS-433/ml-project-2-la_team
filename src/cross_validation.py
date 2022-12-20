"""
@Authors Kilian Raude, Colin Pelletier, Joris Monnet

File used to run a cross validation
"""

import numpy as np

from .metrics import accuracy, f1_score

from implementations import (
    compute_mse,
    compute_log_loss,
    reg_logistic_regression,
    ridge_regression,
    sigmoid,
)


def cross_validation(
    y,
    x,
    k_indices,
    k,
    lambda_,
    is_regression,
    initial_w=None,
    degree=1,
    max_iters=0,
    gamma=0,
    threshold=0,
):
    """return the loss of ridge regression for a fold corresponding to k_indices

    Args:
        y:          shape=(N,)
        x:          shape=(N,)
        k_indices:  2D array returned by build_k_indices()
        k:          scalar, the k-th fold (N.B.: not to confused with k_fold which is the fold nums)
        lambda_:    scalar, cf. ridge_regression()
        degree:     scalar, cf. build_poly()

    Returns:
        train and test root mean square errors rmse = sqrt(2 mse)
    """
    tr_indice = k_indices[~(np.arange(k_indices.shape[0]) == k)]
    tr_indice = tr_indice.reshape(-1)
    te_indice = k_indices[k]
    x_tr = x[tr_indice]
    x_te = x[te_indice]
    y_tr = y[tr_indice]
    y_te = y[te_indice]

    w = 0
    loss_tr = {}
    loss_te = {}

    # add polynomial degree
    xt_tr = build_poly(x_tr, degree)  # if degree=1, add the offset
    xt_te = build_poly(x_te, degree)

    if is_regression:
        # w, loss_train = ridge_regression(y_tr, xt_tr, lambda_)
        w, loss_train = ridge_regression(y_tr, xt_tr, lambda_)

        y_pred_tr = predict_reg(w, xt_tr, threshold=threshold)
        y_pred_te = predict_reg(w, xt_te, threshold=threshold)
        loss_test = compute_mse(y_te, xt_te, w)
    else:
        w, loss_train = reg_logistic_regression(
            y_tr, xt_tr, lambda_, initial_w, max_iters, gamma
        )
        print("fold {} loss_tr {}".format(k, loss_train))

        y_pred_tr = predict_log(w, xt_tr)
        y_pred_te = predict_log(w, xt_te)
        loss_test = compute_log_loss(y_te, xt_te, w)
        print("fold {} loss_tr {}".format(k, loss_train))

    # compute scores
    loss_tr["acc"] = accuracy(y_tr, y_pred_tr)
    loss_tr["f1"] = f1_score(y_tr, y_pred_tr)
    loss_tr["loss"] = loss_train

    loss_te["acc"] = accuracy(y_te, y_pred_te)
    loss_te["f1"] = f1_score(y_te, y_pred_te)
    loss_te["loss"] = loss_test

    return loss_tr, loss_te


def run_cross_validation(
    y,
    x,
    k_fold,
    is_regression,
    lambdas=[0.0],
    gammas=[0.0],
    initial_w=None,
    degrees=[1],
    max_iters=0,
    seed=2,
):
    """cross validation over regularisation parameter lambda.

    Args:
        degree: integer, degree of the polynomial expansion
        k_fold: integer, the number of folds
        lambdas: shape = (p, ) where p is the number of values of lambda to test
        is_regression: boolean
    Returns:
        best_lambda : scalar, value of the best lambda
        best_rmse : scalar, the associated root mean squared error for the best lambda
    """
    res = []
    best_res = {
        "lambda": lambdas[0],
        "gamma": gammas[0],
        "degree": degrees[0],
        "acc": -1,
        "f1": -1,
    }

    for gamma in gammas:
        for lambda_ in lambdas:
            for degree in degrees:
                # define lists to store the loss of training data and test data
                k_fold_res = {"lambda": lambda_, "gamma": gamma, "degree": degree}

                k_fold_res_tr_acc = []
                k_fold_res_te_acc = []

                k_fold_res_tr_f1 = []
                k_fold_res_te_f1 = []

                k_fold_res_tr_loss = []
                k_fold_res_te_loss = []

                # run k predictions
                for k in range(k_fold):
                    loss_tr, loss_te = cross_validation(
                        y,
                        x,
                        build_k_indices(y, k_fold, seed),
                        k,
                        lambda_,
                        is_regression,
                        initial_w,
                        degree,
                        max_iters,
                        gamma,
                    )

                    k_fold_res_tr_acc.append(loss_tr["acc"])
                    k_fold_res_te_acc.append(loss_te["acc"])

                    k_fold_res_tr_f1.append(loss_tr["f1"])
                    k_fold_res_te_f1.append(loss_te["f1"])

                    k_fold_res_tr_loss.append(loss_tr["loss"])
                    k_fold_res_te_loss.append(loss_te["loss"])

                # add results
                k_fold_res["tr"] = {
                    "acc": np.array(k_fold_res_tr_acc).mean(),
                    "f1": np.array(k_fold_res_tr_f1).mean(),
                    "loss": np.array(k_fold_res_tr_loss).mean(),
                }

                k_fold_res["te"] = {
                    "acc": np.array(k_fold_res_te_acc).mean(),
                    "f1": np.array(k_fold_res_te_f1).mean(),
                    "loss": np.array(k_fold_res_te_loss).mean(),
                }

                # set the best result
                if k_fold_res["te"]["acc"] > best_res["acc"]:
                    best_res["lambda"] = lambda_
                    best_res["gamma"] = gamma
                    best_res["degree"] = degree
                    best_res["acc"] = k_fold_res["te"]["acc"]
                    best_res["f1"] = k_fold_res["te"]["f1"]

                res.append(k_fold_res)

    return res, best_res


def build_poly(x, degree):
    """Polynomial basis functions for input data x, for j=0 up to j=degree."""
    poly = np.ones((len(x), 1))
    for deg in range(1, degree + 1):
        poly = np.c_[poly, np.power(x, deg)]
    return poly


def build_k_indices(y, k_fold, seed):
    """build k indices for k-fold.

    Args:
        y:      shape=(N,)
        k_fold: K in K-fold, i.e. the fold num
        seed:   the random seed

    Returns:
        A 2D array of shape=(k_fold, N/k_fold) that indicates the data indices for each fold

    >>> build_k_indices(np.array([1., 2., 3., 4.]), 2, 1)
    array([[3, 2],
           [0, 1]])
    """
    num_row = y.shape[0]
    interval = int(num_row / k_fold)
    np.random.seed(seed)
    indices = np.random.permutation(num_row)
    k_indices = [indices[k * interval : (k + 1) * interval] for k in range(k_fold)]
    return np.array(k_indices)


def predict_log(w, x):
    """ "
    Predict with a sigmoid
    """
    assert w.shape[0] == x.shape[1]
    y_pred = sigmoid(x @ w)

    y_pred[y_pred <= 0.5] = -1
    y_pred[y_pred > 0.5] = 1

    return y_pred


def predict_reg(w, x, threshold=0.0):
    """ "
    Add lambda_ to the prediction
    """
    assert w.shape[0] == x.shape[1]
    y_pred = x @ w

    y_pred[y_pred <= threshold] = -1
    y_pred[y_pred > threshold] = 1

    return y_pred
