# Tools to pre-process images during the ML pipeline, 
# import images and display them.
#
# Author: Amy Jang, Software Engineering Intern at Google (TensorFlow). 
#   Kaggle profile: https://www.kaggle.com/amyjang  
#
# Update: Colin Pelletier, Joris Monnet and Kilian Raude
import tensorflow as tf
import os

#
# Image import and pre-processing
#

class ImageTools:

    def __init__(self, image_size, num_parallel_calls):
        self.image_size = image_size
        self.num_parallel_calls = num_parallel_calls


    def get_label(self, file_path):
        # convert the path to a list of path components
        parts = tf.strings.split(file_path, os.path.sep)
        # The second to last is the class-directory
        return parts[-2] != "Normal"


    def decode_img(self, img):
        # convert the compressed string to a 3D uint8 tensor
        img = tf.image.decode_jpeg(img, channels=3)
        # Use `convert_image_dtype` to convert to floats in the [0,1] range.
        img = tf.image.convert_image_dtype(img, tf.float32)
        # resize the image to the desired size.
        return tf.image.resize(img, self.image_size)


    def process_path(self, file_path):
        label = self.get_label(file_path)
        # load the raw data from the file as a string
        img = tf.io.read_file(file_path)
        img = self.decode_img(img)
        return img, label

    
    def load_images_from_filenames(self, ds):
        return ds.map(self.process_path, num_parallel_calls=self.num_parallel_calls)


#
# Batch import
#

def prepare_for_training(ds, batch_size, buffer_size, cache=True, shuffle_buffer_size=1000):
    # This is a small dataset, only load it once, and keep it in memory.
    # use `.cache(filename)` to cache preprocessing work for datasets that don't
    # fit in memory.
    if cache:
        if isinstance(cache, str):
            ds = ds.cache(cache)
        else:
            ds = ds.cache()

    ds = ds.shuffle(buffer_size=shuffle_buffer_size)

    # Repeat forever
    ds = ds.repeat()

    ds = ds.batch(batch_size)

    # `prefetch` lets the dataset fetch batches in the background while the model
    # is training.
    #ds = ds.prefetch(buffer_size=AUTOTUNE) TODO remove it
    ds = ds.prefetch(buffer_size=buffer_size)

    return ds