import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class Actor_Network(object, env, sess, batch_size=32, tau=0.125, learning_rate=1e-3):
    def __init__(self):
        self.env = env
        self.sess = sess

        self.obs_dim = 3
        self.hidden_dim = 32
        self.act_dim = 3
        self.lr = learning_rate

        # For training
        # Instantiate an optimizer.
        optimizer = keras.optimizers.Adam(learning_rate=self.rl)
        # Instantiate a loss function.



    def create_actor(self):
        model = keras.Sequential()
        model.add(keras.Input(shape=(3,)))
        model.add(layers.Dense(self.hidden_dim, activation="relu"))
        model.add(layers.Dense(self.hidden_dim, activation="relu"))
        model.add(layers.Dense(self.hidden_dim, activation="relu"))
        model.add(layers.Dense(self.act_dim, activation="tanh"))
        #model.summary()
        return model, model.trainable_weights, model.input

    def train

        
        
        

