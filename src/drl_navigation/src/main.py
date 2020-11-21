#!/usr/bin/env python3

import rospy
import time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import argparse
#from tensorflow import keras 
from tensorflow.keras.models import model_from_json, Model,load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
import os
import json
import pdb
import argparse
from Replay_Buffer import Replay_Buffer
from Actor_Network import Actor_Network
from Critic_Network import Critic_Network
import tensorflow.keras.backend as K

timestr = time.strftime("%Y%m%d-%H%M%S")
save_path = 'saved_models_rohit_' + timestr

def ou_func(x, mu, theta, sigma=0.3):
    return theta * (mu - x) + sigma * np.random.randn(1)

def train_quad(debug=True):
    
    env = environment.Environment(debug)  # Rohit's custom environment

    obs_dim = env.num_states
    act_dim = env.num_actions

    buffer_size = 5000
    batch_size = 32
    gamma = 0.98
    tau = 0.001

    np.random.seed(1337)

    vision = False

    explore = 100000
    eps_count = 1000
    max_steps = 100000
    reward = 0
    done = False
    epsilon = 1
    indicator = 0

    plot_state = False
    plot_reward = True

    episode_rewards = []
    episode = []

    # Configue tensorflow CPU/GPU
    # TODO

    # Define actor, critic and buffer
    actor = Actor_Network(env, sess)
    critic = Critic_Network(env, sess)
    replay_buffer = Replay_Buffer()
