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
import myquadcopter_env as environment

timestr = time.strftime("%Y%m%d-%H%M%S")
save_path = 'saved_models_' + timestr

def ou_func(x, mu, theta, sigma=0.3):
    return theta * (mu - x) + sigma * np.random.randn(1)

def train_quad(debug=True):
    
    env = environment.QuadCopterEnv(debug)  # Rohit's custom environment

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

    # Save location
    save_dir = os.path.join(os.getcwd(), save_path)
    if not os.path.isdir():
        os.makedirs(save_dir)
    os.chdir(save_dir)

    # Plot total reward
    plt.ion()
    plt.title('Training Curve')
    plt.xlabel('Episodes')
    plt.ylabel('Total Reward')
    plt.grid()
    
    # Episode loop
    for epi in range (eps_count):
        # Receive initial observation state
        s_t = env._reset() # Initial position info
        s_t = np.asarray(s_t)
        total_reward = 0
        done = False
        step = 0

        # Step loop
        while(done == False):
            if step > 200: # Episode length is 200 steps
                break

            step += 1
            if debug:
                print('--------------------------------')
                print('step: {}'.format(step))

            loss = 0
            epsilon -= 1.0/explore # It's a constant

            a_t = np.zeros([1, act_dim])
            noise_t = np.zeros([1, act_dim])

            # Select action acoording to current policy and exploration noise
            a_t_original = actor.model.predict(s_t.reshape(1, s_t.shape[0]))

            noise_t[0][0] = max(epsilon,0) * ou_func(a_t_original[0][0],  0.0 , 0.60, 0.30)
            noise_t[0][1] = max(epsilon,0) * ou_func(a_t_original[0][1],  0.0 , 0.60, 0.30)
            noise_t[0][2] = max(epsilon,0) * ou_func(a_t_original[0][2],  0.0 , 0.60, 0.30)

            a_t[0][0] = a_t_original[0][0] + noise_t[0][0]
            a_t[0][1] = a_t_original[0][1] + noise_t[0][1]
            a_t[0][2] = a_t_original[0][2] + noise_t[0][2]

            s_t1, r_t, done, _ = env._step(a_t[0])
            s_t1 = np.asarray(s_t1)

            # Add current data to replay buffer
            replay_buffer.add(s_t, a_t[0], r_t, s_t1, done)

            # Sample from replay buffer
            batch = replay_buffer.sample_batch()
            states = np.asarray([e[0] for e in batch])
            actions = np.asarray([e[1] for e in batch])
            rewards = np.asarray([e[2] for e in batch])
            new_states = np.asarray([e[3] for e in batch])
            dones = np.asarray([e[4] for e in batch])
            y_t = np.asarray([e[1] for e in batch]) # Just make a empty array has same shape

            # Calculate target Q values (What is target Q values)
            target_q_values = critic.target_model.predict([new_states, actor.target_model.predict(new_states)])
            
            # y_t is like the label of 
            for k in range (len(batch)):
                if dones[k]:
                    y_t[k] = rewards[k]
                else:
                    y_t[k] = rewards[k] + gamma*target_q_values[k]

            # Train critic model
            loss += critic.model.train_on_batch([states, actions], y_t)
            a_for_grad = actor.model.predict(states)
            grads = critic.gradients(states, a_for_grad)
            actor.train(states, grads)
            actor.target_train()
            critic.target_train()

            total_reward += r_t
            s_t = s_t1

        # One step finish, save models
        if ((epi+1)%50 == 0):
            a_model_name = '%d_actor_model.h5' %(epi+1)
            c_model_name = '%d_critic_model.h5' %(epi+1)
            filepath = os.path.join(save_dir, a_model_name)
            actor.model.save(a_model_name)
            critic.model.save(c_model_name)
        print('episode: {}, num_steps: {}, total rewards: {:.2f}, final state: ({:.2f},{:.2f},{:.2f})'.format(epi+1, step, total_reward, s_t[0], s_t[1], s_t[2]))

        if plot_reward:
            episode_rewards.append(total_reward)
            episode.append(epi+1)
            plt.plot(episode, episode_rewards, 'b')
            plt.pause(0.001)

    plt.savefig("Training Curve.png")

import signal, sys
def signal_handler(signal, frame):
    reason =  'Because'
    rospy.signal_shutdown(reason)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    rospy.init_node('quad', anonymous=True, disable_signals=True)
    debug = 1
    train_quad(debug)
    



    


                

    
