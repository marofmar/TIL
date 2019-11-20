'''
However, I used tensorflow to load Iris dataset!
'''

__future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd
import numpy as np 


CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength' , 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

train_path = tf.keras.utils.get_file(
    "iris_training.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv")
test_path = tf.keras.utils.get_file(
    "iris_test.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv")

train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)


def pca(x):
    x = (x-x.mean(axis = 0)) 
    num_observations, num_dimensions = x.shape 

    u, s, vh = np.linalg.svd(x) 
    return u, s, vh
    
u, s, vh = pca(train)
print(u.shape,s.shape, vh.shape )
