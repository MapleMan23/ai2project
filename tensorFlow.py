
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import random
import time

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
data = []
seasons = ["2008","2009","2010", "2012","2013","2014"]
batch_size = 1024

for i,season in enumerate(seasons):
    data.append(np.genfromtxt(f"train{season}.csv", delimiter=','))

data_csv = np.concatenate(data)
random.shuffle(data_csv) 
train_csv = data_csv[:int(len(data_csv) * 0.70)]
test_csv = data_csv[len(train_csv):]

train_data = train_csv[:,1:-1]
train_labels = train_csv[:,-1]

test_data = test_csv[:,1:-1]
test_labels = test_csv[:,-1]

acc = []

t = time.time()

num_train, num_features = train_data.shape
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(num_features,)),
    keras.layers.Dense(int(num_features), activation=tf.nn.relu),
    keras.layers.Dropout(0.4),
    # keras.layers.Dense(int(num_features/2), activation=tf.nn.relu),
    #keras.layers.Dense(num_features/4, activation=tf.nn.relu),
    # keras.layers.Dense(2, activation=tf.nn.relu),
    keras.layers.Dense(1, activation="sigmoid")
])
tf.keras.utils.plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

convergence = keras.callbacks.EarlyStopping(patience= 180)

model.compile(
    optimizer="adam",
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(train_data, train_labels, epochs=(1000), batch_size= batch_size, verbose = 2, validation_data = (test_data, test_labels), callbacks=[convergence])

test_loss,test_acc = model.evaluate(test_data,test_labels)
acc.append(test_acc)

print("Acc: ",acc)
print("Time: ",time.time() - t)

print(history.history.keys())
#  "Accuracy"
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Neural Network Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Neural Network Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()