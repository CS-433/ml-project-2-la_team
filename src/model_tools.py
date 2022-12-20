# Tools to define the architecture of the model
#
# Author: Amy Jang, Software Engineering Intern at Google (TensorFlow).
#   Kaggle profile: https://www.kaggle.com/amyjang
#
# Update: Colin Pelletier, Joris Monnet and Kilian Raude

# TODO absolutely change the architecture and create
# a subclass of sequential. This is much more clean!!

#
# TEXT ROM THE NOTEBOOK
#

# Code for the model:
# To make our model more modular and easier to understand, let's define some
# blocks. As we're building a convolution neural network, we'll create a
# convolution block and a dense layer block.
# The architecture for this CNN has been inspired by this [article](https://towardsdatascience.com/deep-learning-for-detecting-pneumonia-from-x-ray-images-fc9a3d9fdba8).

#
# TEXT ROM THE NOTEBOOK END
#
import tensorflow as tf
import matplotlib.pyplot as plt
import json
import numpy as np

#
# ARCHITECTURE
#

# def conv_block(filters):
#     """

#     """
#     block = tf.keras.Sequential([
#         tf.keras.layers.SeparableConv2D(filters, 3, activation='relu', padding='same'),
#         tf.keras.layers.SeparableConv2D(filters, 3, activation='relu', padding='same'),
#         tf.keras.layers.BatchNormalization(),
#         tf.keras.layers.MaxPool2D()
#     ]
#     )

#     return block

# def dense_block(units, dropout_rate):
#     """

#     """
#     block = tf.keras.Sequential([
#         tf.keras.layers.Dense(units, activation='relu'),
#         tf.keras.layers.BatchNormalization(),
#         tf.keras.layers.Dropout(dropout_rate)
#     ])

#     return block


def build_model(image_size):
    """
        Text from the notebook
        The following method will define the function to build our model for us.
        The Dropout layers are important as they "drop out," hence the name,
        certain nodes to reduce the likelikhood of the model overfitting. 
        We want to end the model with a Dense layer of one node, as this will 
        be the output that determines if an X-ray shows an image of pneumonia.
    """
    model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(image_size[0], image_size[1], 3)),
            tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same"),
            tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same"),
            tf.keras.layers.MaxPool2D(),
            # conv_block(32),
            tf.keras.layers.SeparableConv2D(32, 3, activation="relu", padding="same"),
            tf.keras.layers.SeparableConv2D(32, 3, activation="relu", padding="same"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPool2D(),
            # conv_block(64),
            tf.keras.layers.SeparableConv2D(64, 3, activation="relu", padding="same"),
            tf.keras.layers.SeparableConv2D(64, 3, activation="relu", padding="same"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPool2D(),
            # conv_block(128),
            tf.keras.layers.SeparableConv2D(128, 3, activation="relu", padding="same"),
            tf.keras.layers.SeparableConv2D(128, 3, activation="relu", padding="same"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPool2D(),
            tf.keras.layers.Dropout(0.2),
            # conv_block(256),
            tf.keras.layers.SeparableConv2D(256, 3, activation="relu", padding="same"),
            tf.keras.layers.SeparableConv2D(256, 3, activation="relu", padding="same"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPool2D(),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Flatten(),
            # dense_block(512, 0.7),
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.7),
            # dense_block(128, 0.5),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.5),
            # dense_block(64, 0.3),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    # model = tf.keras.Sequential(
    #     [
    #     tf.keras.Input(shape=(image_size[0], image_size[1], 3)),

    #     tf.keras.layers.Conv2D(16, 3, activation='relu', padding='same'),
    #     tf.keras.layers.Conv2D(16, 3, activation='relu', padding='same'),
    #     tf.keras.layers.MaxPool2D(),

    #     conv_block(32),
    #     conv_block(64),

    #     conv_block(128),
    #     tf.keras.layers.Dropout(0.2),

    #     conv_block(256),
    #     tf.keras.layers.Dropout(0.2),

    #     tf.keras.layers.Flatten(),
    #     dense_block(512, 0.7),
    #     dense_block(128, 0.5),
    #     dense_block(64, 0.3),

    #     tf.keras.layers.Dense(1, activation='sigmoid')
    # ])

    return model


#
# FINETUNING
#


def exponential_decay(lr0, s):
    """

    """

    def exponential_decay_fn(epoch):
        return lr0 * 0.1 ** (epoch / s)

    return exponential_decay_fn


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

    """
    # make sure to cast float32 values to string
    for key, lst in history_dict.items():
        history_dict[key] = [str(val) for val in lst]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history_dict, f)
        print("History successfully written in {}".format(filename))


def load_history(filename):
    """

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
