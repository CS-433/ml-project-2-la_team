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

def conv_block(filters):
    """

    """
    block = tf.keras.Sequential([
        tf.keras.layers.SeparableConv2D(filters, 3, activation='relu', padding='same'),
        tf.keras.layers.SeparableConv2D(filters, 3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D()
    ]
    )
    
    return block

def dense_block(units, dropout_rate):
    """

    """
    block = tf.keras.Sequential([
        tf.keras.layers.Dense(units, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(dropout_rate)
    ])
    
    return block

def build_model(image_size):
    """
        Text from the notebook
        The following method will define the function to build our model for us.
        The Dropout layers are important as they "drop out," hence the name,
        certain nodes to reduce the likelikhood of the model overfitting. 
        We want to end the model with a Dense layer of one node, as this will 
        be the output that determines if an X-ray shows an image of pneumonia.
    """
    model = tf.keras.Sequential([
        tf.keras.Input(shape=(image_size[0], image_size[1], 3)),
        
        tf.keras.layers.Conv2D(16, 3, activation='relu', padding='same'),
        tf.keras.layers.Conv2D(16, 3, activation='relu', padding='same'),
        tf.keras.layers.MaxPool2D(),
        
        conv_block(32),
        conv_block(64),
        
        conv_block(128),
        tf.keras.layers.Dropout(0.2),
        
        conv_block(256),
        tf.keras.layers.Dropout(0.2),
        
        tf.keras.layers.Flatten(),
        dense_block(512, 0.7),
        dense_block(128, 0.5),
        dense_block(64, 0.3),
        
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    return model


#
# FINETUNING
#

def exponential_decay(lr0, s):
    """

    """
    def exponential_decay_fn(epoch):
        return lr0 * 0.1 **(epoch / s)
    return exponential_decay_fn


#
# VISUALIZATION
#

def plot_model_performances(history, metrics=['precision', 'recall', 'accuracy', 'loss'], suptitle='Model Metrics', figsize=(20, 3)):
    """

    """
    fig, ax = plt.subplots(1, 4, figsize=figsize)
    ax = ax.ravel()

    for i, metric in enumerate(['precision', 'recall', 'accuracy', 'loss']):
        ax[i].plot(history.history[metric])
        ax[i].plot(history.history['val_' + metric])
        ax[i].set_title('Model {}'.format(metric))
        ax[i].set_xlabel('epochs')
        ax[i].set_ylabel(metric)
        ax[i].legend(['train', 'val'])
    plt.plot()


#
# EXPORT
#

def save_history(filename, history_dict):
    """

    """
    # make sure to cast float32 values to string
    for key, lst in history_dict.items():
        history_dict[key] = [str(val) for val in lst]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(history_dict, f)
        print("History successfully written in {}".format(filename))
        


def load_history(filename):
    """

    """
    with open(filename, 'r', encoding='utf-8') as f:
        history_dict = json.load(f)

        # cast string values to float32
        for key, lst in history_dict.items():
            history_dict[key] = [np.float32(val) for val in lst]


def predict_and_save_predictions(model, test_ds_batch, test_filenames, filename):
    """

    """
    # TODO improve that

    # predict and get predicted label by applying a threshold
    y_pred = model.predict(test_ds_batch)
    y_pred[y_pred >= 0.5] = 1
    y_pred[y_pred < 0.5] = 0
    y_pred = y_pred.astype(np.int32)

    y_true = np.array(['Normal' in name for name in test_filenames]).astype(np.int32)

    with open(filename, encoding='utf-8', mode='w') as f:
        #y_true;y_pred
        for i in range(y_true.shape[0]):
            f.write("{};{}\n".format(y_true[i], y_pred[i][0]))

        print("Predictions successfully written in {}".format(filename))

