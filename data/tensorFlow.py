
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

train_csv = np.genfromtxt("data/train.csv", delimiter=',')
train_data = train_csv[1:-2]
train_labels = train_csv[-1]

test_csv = np.genfromtxt("data/test.csv", delimiter=',')
test_data = test_csv[1:-2]
test_labels = test_csv[-1]

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(1,240)),
    keras.layers.Dense(240, activation=tf.nn.relu),
    keras.layers.Dense(240, activation=tf.nn.relu),
    keras.layers.Dense(240, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(
    optimizer='SGD',
    loss='mean_squared_error',
    metric=['accuracy']
)

model.fit(train_data, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_data,test_labels)
print('Test accuracy: ', test_acc)
