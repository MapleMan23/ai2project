
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import random

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
data = []
seasons = ["2008","2009","2010"]
maxlen = 0
for i,season in enumerate(seasons):
    data.append(np.genfromtxt(f"train{season}.csv", delimiter=','))
    if len(data[i][0]) > maxlen:
        maxlen = len(data[i][0])

data_csv = np.concatenate(data)
print(data_csv)
random.shuffle(data_csv)
train_csv = data_csv[:int(len(data_csv) * 0.70)]
test_csv = data_csv[len(train_csv):]

train_data = train_csv[:,1:-1]
train_labels = train_csv[:,-1]

test_data = test_csv[:,1:-1]
test_labels = test_csv[:,-1]

acc = []
for i in range(0,11):

    num_train, num_features = train_data.shape
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(num_features,)),
        keras.layers.Dense(num_features, activation=tf.nn.relu),
        keras.layers.Dense(num_features, activation=tf.nn.relu),
        keras.layers.Dense(num_features, activation=tf.nn.relu),
        keras.layers.Dense(2, activation=tf.nn.softmax),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    model.compile(
        optimizer='Nadam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    model.fit(train_data, train_labels, epochs=(30+i))
    test_loss, test_acc = model.evaluate(test_data,test_labels)
    acc.append(test_acc)
    model.reset_states()

print(acc)