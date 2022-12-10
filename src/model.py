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


def conv_block(filters):
    block = tf.keras.Sequential([
        tf.keras.layers.SeparableConv2D(filters, 3, activation='relu', padding='same'),
        tf.keras.layers.SeparableConv2D(filters, 3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D()
    ]
    )
    
    return block

def dense_block(units, dropout_rate):
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


def exponential_decay(lr0, s):
    def exponential_decay_fn(epoch):
        return lr0 * 0.1 **(epoch / s)
    return exponential_decay_fn