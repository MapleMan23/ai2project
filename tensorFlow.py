
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import random

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

data2008 = np.genfromtxt("train2008.csv", delimiter=',')
data2009 = np.genfromtxt("train2009.csv", delimiter=',')
# data2010 = np.genfromtxt("train2010.csv", delimiter=',')
# print(data2010.shape)

data_csv = np.concatenate([data2008,data2009])

random.shuffle(data_csv)
train_csv = data_csv[:int(len(data_csv) * 0.70)]
test_csv = data_csv[len(train_csv):]

train_data = train_csv[:,1:-1]
train_labels = train_csv[:,-1]

test_data = test_csv[:,1:-1]
test_labels = test_csv[:,-1]

num_train, num_features = train_data.shape
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(num_features,)),
    keras.layers.Dense(num_features, activation=tf.nn.relu),
    keras.layers.Dense(num_features, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax),
    keras.layers.Dense(1, activation=tf.nn.sigmoid)
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(train_data, train_labels, epochs=20)

test_loss, test_acc = model.evaluate(test_data,test_labels)
print('Test accuracy: ', test_acc)
