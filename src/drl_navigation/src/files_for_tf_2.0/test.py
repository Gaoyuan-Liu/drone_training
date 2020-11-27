import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

hidden_dim = 32
act_dim = 3
model = keras.Sequential()
model.add(keras.Input(shape=(3,)))
model.add(layers.Dense(hidden_dim, activation="relu"))
model.add(layers.Dense(hidden_dim, activation="relu"))
model.add(layers.Dense(hidden_dim, activation="relu"))
model.add(layers.Dense(act_dim, activation="tanh"))

#model.summary()
#input = tf.ones((1,3))
#y = model(input)
print(model.inputs.shape)