"""
@Author Amy Jang, Software Engineering Intern at Google (TensorFlow). 
        Kaggle profile: https://www.kaggle.com/amyjang  

@Update Colin Pelletier, Joris Monnet, Kilian Raude

This file contains the helpers to plot and export model predictions

"""
import tensorflow as tf
import matplotlib.pyplot as plt
import json
import numpy as np


#
# METRICS
#
def f1_score(y_true, y_pred):
    """
    Compute f1 score during training
    Source: https://aakashgoel12.medium.com/how-to-add-user-defined-function-get-f1-score-in-keras-metrics-3013f979ce0d
    """
    from keras.callbacks import Callback, ModelCheckpoint
    from keras.models import Sequential, load_model
    from keras.layers import Dense, Dropout
    from keras.wrappers.scikit_learn import KerasClassifier
    import keras.backend as K

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())

    return f1_val


#
# VISUALIZATION
#


def plot_model_performances(
    history,
    metrics=["precision", "recall", "accuracy", "loss"],
    suptitle="Model Metrics",
    figsize=(20, 3),
):
    """
    Plot accuracy, recall, precision and loss
    """
    fig, ax = plt.subplots(1, 4, figsize=figsize)
    ax = ax.ravel()

    for i, metric in enumerate(["precision", "recall", "accuracy", "loss"]):
        ax[i].plot(history.history[metric])
        ax[i].plot(history.history["val_" + metric])
        ax[i].set_title("Model {}".format(metric))
        ax[i].set_xlabel("epochs")
        ax[i].set_ylabel(metric)
        ax[i].legend(["train", "val"])
    plt.plot()


#
# EXPORT AND LOAD
#


def save_history(filename, history_dict):
    """
    Save training history as a json file
    """
    # make sure to cast float32 values to string
    for key, lst in history_dict.items():
        history_dict[key] = [str(val) for val in lst]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history_dict, f)
        print("History successfully written in {}".format(filename))


def load_history(filename):
    """
    Load training history from the json file (preferably saved with save_history)
    """
    with open(filename, "r", encoding="utf-8") as f:
        history_dict = json.load(f)

        # cast string values to float32
        for key, lst in history_dict.items():
            history_dict[key] = [np.float32(val) for val in lst]


def read_predictions(input_file):
    """
    Read the predictions file and returns numpy arrays of y_true and y_pred
    """
    y_true = []
    y_pred = []

    with open(input_file, "r", encoding="utf-8") as f:
        # Iterate over the input data
        for line in f.readlines():
            label_true, label_pred = line.split(";")
            y_true.append(int(label_true))
            y_pred.append(float(label_pred))

    return np.array(y_true), np.array(y_pred)
