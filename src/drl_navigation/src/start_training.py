#!/usr/bin/env python3

'''
    Training code made by Ricardo Tellez <rtellez@theconstructsim.com>
    Based on many other examples around Internet
    Visit our website at www.theconstruct.ai
'''
import gym
import time
import numpy
import random
import time

import pickle
from gym import wrappers

# ROS packages required
import rospy
import rospkg

# import our training environment
import myquadcopter_env



if __name__ == '__main__':
    
    rospy.init_node('drone_gym', anonymous=True)

    # Create the Gym environment
    env = gym.make('QuadcopterLiveShow-v0')
    rospy.loginfo ( "Gym environment done")
    

    # Set the logging system
    rospack = rospkg.RosPack()
    pkg_path = rospack.get_path('drone_training')
    outdir = pkg_path + '/training_results'
    env = wrappers.Monitor(env, outdir, force=True) 
    rospy.loginfo ( "Monitor Wrapper started")

    last_time_steps = numpy.ndarray(0)

    # Loads parameters from the ROS param server
    # Parameters are stored in a yaml file inside the config directory
    # They are loaded at runtime by the launch file
    Alpha = rospy.get_param("/alpha")
    Epsilon = rospy.get_param("/epsilon")
    Gamma = rospy.get_param("/gamma")
    epsilon_discount = rospy.get_param("/epsilon_discount")
    nepisodes = rospy.get_param("/nepisodes")
    nsteps = rospy.get_param("/nsteps")

    # Initialises the algorithm that we are going to use for learning


    start_time = time.time()
    highest_reward = 0

    # Starts the main training loop: the one about the episodes to do
    for x in range(nepisodes):
        rospy.loginfo("STARTING Episode #"+str(x))
        
        cumulated_reward = 0  
        done = False
        
        # Initialize the environment and get first state of the robot
        observation = env.reset()
        
        
        # Show on screen the actual situation of the robot
        #env.render()
        
        # for each episode, we test the robot for nsteps
        for i in range(nsteps):

            # Pick an action based on the current state

            action = [0, 0, 0.05]
            
            # Execute the action in the environment and get feedback
            observation, reward, done, info = env.step(action)
            cumulated_reward += reward
            if highest_reward < cumulated_reward:
                highest_reward = cumulated_reward

            nextState = ''.join(map(str, observation)) # Make state a string

            # Make the algorithm learn based on the results
 
            rospy.loginfo ("step number is " + str(i))
            #rospy.loginfo ("choose action " + str(action))
            #rospy.loginfo ("current state is " + str(observation))
            if not(done):
                state = nextState
            else:
                rospy.loginfo ("DONE")
                last_time_steps = numpy.append(last_time_steps, [int(i + 1)])
                break

        m, s = divmod(int(time.time() - start_time), 60)
        h, m = divmod(m, 60)
        

    
   

    l = last_time_steps.tolist()
    l.sort()

    #print("Parameters: a="+str)
    rospy.loginfo("Overall score: {:0.2f}".format(last_time_steps.mean()))
    #rospy.loginfo("Best 100 score: {:0.2f}".format(reduce(lambda x, y: x + y, l[-100:]) / len(l[-100:])))    
    # Save the final qtable
    
    env.close()
