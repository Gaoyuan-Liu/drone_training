#!/usr/bin/env python

import gym
import rospy
import time
import numpy as np
import tf
import time
import json
from gym import utils, spaces
from geometry_msgs.msg import Twist, Vector3Stamped, Pose, PoseStamped
from hector_uav_msgs.msg import Altimeter
from sensor_msgs.msg import Imu
from std_msgs.msg import Empty as EmptyTopicMsg
from gym.utils import seeding
from gym.envs.registration import register
from gazebo_connection import GazeboConnection

#register the training environment in the gym as an available one
reg = register(
    id='QuadrotorRLControl-v2',
    entry_point='navigation_env_3d:QuadrotorEnv',
    max_episode_steps=30,
    )


class QuadrotorEnv(gym.Env):

    def __init__(self):
        
        # We assume that a ROS node has already been created
        # before initialising the environment
        
        self.position_pub = rospy.Publisher('/drone/command/pose', PoseStamped, queue_size=100)
        
        # gets training parameters from param server
        self.speed_value = rospy.get_param("/speed_value")
        self.desired_pose = Pose()
        self.desired_pose.position.z = rospy.get_param("/desired_pose/z")
        self.desired_pose.position.x = rospy.get_param("/desired_pose/x")
        self.desired_pose.position.y = rospy.get_param("/desired_pose/y")
        self.running_step = rospy.get_param("/running_step")
        self.max_incl = rospy.get_param("/max_incl")
        self.max_altitude = rospy.get_param("/max_altitude")
        
        # stablishes connection with simulator
        self.gazebo = GazeboConnection()
        
        self.action_space = spaces.Discrete(7) #Forward,Backward,Left,Right,Still
        self.reward_range = (-np.inf, np.inf)

        self.seed()
        

    # A function to initialize the random generator
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
        
    # Resets the state of the environment and returns an initial observation.
    def reset(self):
        
        # 1st: resets the simulation to initial values
        self.gazebo.resetSim()

        # 2nd: Unpauses simulation
        self.gazebo.unpauseSim()

        # 3rd: resets the robot to initial conditions
        self.check_topic_publishers_connection()
        self.init_desired_pose()
        self.current_position = Pose()
        self.current_command = PoseStamped()
        self.current_command.pose.position.x = 0.5
        self.current_command.pose.position.y = 0.5
        self.current_command.pose.position.z = 5.5
        # 4th: takes an observation of the initial condition of the robot
        data_pose = self.take_observation()
        observation = [self.calculate_state_number(data_pose.position.x, data_pose.position.y, data_pose.position.z)]
        
        # 5th: pauses simulation
        self.gazebo.pauseSim()

        return observation

    def step(self, action):

        # Given the action selected by the learning algorithm,
        # we perform the corresponding movement of the robot
        
        # 1st, we decide which velocity command corresponds
        #current_position = self.take_observation()
        position_cmd = PoseStamped()
        position_cmd.header.frame_id = "world"
        

        if action == 0: #FORWARD
            position_cmd.pose.position.x = self.current_command.pose.position.x + 1
            position_cmd.pose.position.y = self.current_command.pose.position.y
            position_cmd.pose.position.z = self.current_command.pose.position.z 
        elif action == 1: #BACKWARD
            position_cmd.pose.position.x = self.current_command.pose.position.x - 1
            position_cmd.pose.position.y = self.current_command.pose.position.y
            position_cmd.pose.position.z = self.current_command.pose.position.z
        elif action == 2: #RIGHT
            position_cmd.pose.position.x = self.current_command.pose.position.x
            position_cmd.pose.position.y = self.current_command.pose.position.y + 1
            position_cmd.pose.position.z = self.current_command.pose.position.z
        elif action == 3: #LEFT
            position_cmd.pose.position.x = self.current_command.pose.position.x
            position_cmd.pose.position.y = self.current_command.pose.position.y - 1
            position_cmd.pose.position.z = self.current_command.pose.position.z
        elif action == 4: #UP
            position_cmd.pose.position.x = self.current_command.pose.position.x 
            position_cmd.pose.position.y = self.current_command.pose.position.y
            position_cmd.pose.position.z = self.current_command.pose.position.z + 1
        elif action == 5: #DOWN
            position_cmd.pose.position.x = self.current_command.pose.position.x 
            position_cmd.pose.position.y = self.current_command.pose.position.y
            position_cmd.pose.position.z = self.current_command.pose.position.z - 1
        elif action == 6: #still
            position_cmd.pose.position.x = self.current_command.pose.position.x 
            position_cmd.pose.position.y = self.current_command.pose.position.y
            position_cmd.pose.position.z = self.current_command.pose.position.z
        
        if position_cmd.pose.position.z < 0:
            position_cmd.pose.position.z = 0.4

        # Then we send the command to the robot and let it go
        # for running_step seconds
        self.gazebo.unpauseSim()
        self.position_pub.publish(position_cmd)
        #time.sleep(self.running_step) # time per step
        data_pose = self.take_observation()
        self.current_position = data_pose
        
        self.current_command = position_cmd

        # Wait until the drone actually got the command position
        rate = rospy.Rate(100)
        while not self.calculate_state_number(self.current_position.position.x,  self.current_position.position.y, self.current_position.position.z) == self.calculate_state_number(position_cmd.pose.position.x, position_cmd.pose.position.y, position_cmd.pose.position.z):
            self.position_pub.publish(position_cmd)
            data_pose = self.take_observation()
            #if data_pose.position.z < 0.4: 
             #  done = True
            self.current_position = data_pose
            """current_state_number = self.calculate_state_number(self.current_position.position.x,  self.current_position.position.y, self.current_position.position.z)
            command_state_number = self.calculate_state_number(position_cmd.pose.position.x, position_cmd.pose.position.y, position_cmd.pose.position.z)
            rospy.loginfo ("current_state_number is " + str(current_state_number))
            rospy.loginfo ("command_state_number is " + str(command_state_number))"""
            
            rate.sleep()

        self.gazebo.pauseSim()

            

        # finally we get an evaluation based on what happened in the sim
        reward,done = self.process_data(data_pose, self.desired_pose)


        state = [self.calculate_state_number(data_pose.position.x, data_pose.position.y, data_pose.position.z)]
        return state, reward, done, {}


    def take_observation (self):
        data_pose = None
        while data_pose is None:
            try:
                data_pose_raw = rospy.wait_for_message('/drone/ground_truth_to_tf/pose', PoseStamped, timeout=100)
                data_pose = data_pose_raw.pose
            except:
                rospy.loginfo("Current drone pose not ready yet, retrying for getting robot pose")
        
        return data_pose

    def calculate_dist_between_two_Points(self,p_init,p_end):
        a = np.array((p_init.x ,p_init.y, p_init.z))
        b = np.array((p_end.x ,p_end.y, p_end.z))
        
        dist = np.linalg.norm(a-b)
        
        return dist


    def init_desired_pose(self):
        
        current_init_pose = self.take_observation()
        
        self.best_dist = self.calculate_dist_between_two_Points(current_init_pose.position, self.desired_pose.position)
    

    def check_topic_publishers_connection(self):
        
        rate = rospy.Rate(10) # 10hz

        while(self.position_pub.get_num_connections() == 0):
            rospy.loginfo("No susbribers to Cmd_position yet so we wait and try again")
            rate.sleep();
        rospy.loginfo("Cmd_position Publisher Connected")
        

    '''def reset_cmd_position_commands(self):
        # We send an empty null Twist
        position_cmd = PoseStamped()
        position_cmd.pose.position.x = 0
        position_cmd.pose.position.y = 0
        position_cmd.pose.position.z = 0
        self.position_pub.publish(position_cmd)'''

        

    def improved_distance_reward(self, current_pose, desired_pose):
        done = False
        current_state = self.calculate_state_number(current_pose.position.x, current_pose.position.y, current_pose.position.z)
        desired_state = self.calculate_state_number(desired_pose.position.x, desired_pose.position.y, desired_pose.position.z)
        
        current_dist = self.calculate_dist_between_two_Points(current_pose.position, desired_pose.position)
        if current_dist < self.best_dist:
            reward = 100
            self.best_dist = current_dist
        elif current_dist == self.best_dist:
            reward = -10
        else:
            reward = -100

        if current_state == desired_state:
            reward += 1000
            done = True
        
        return reward, done
        
    def process_data(self, data_position, desired_pose):

        done = False
        x_out = data_position.position.x > 5 or data_position.position.x < -5
        y_out = data_position.position.y > 5 or data_position.position.y < -5
        z_out = data_position.position.z > 10 or data_position.position.z < 0.5
        if x_out or y_out or z_out:
            rospy.loginfo ("(Drone flight position is out)")
            done = True
            reward = -200
        else:
            reward, done = self.improved_distance_reward(data_position, desired_pose)

        return reward, done

    def calculate_state_number (self, x, y, z):
        if x < -5:
            x = -4.99
        if x > 5:
            x = 4.99
        if y < -5:
            y = -4.99
        if y > 5:
            y = 4.99
        if z < 0.2:#0.1824 when drone stay ground
            z = 0.2
        if z > 10:
            z = 9.99
        for i in range(10):
            if x >= -5+i and x < -5+i+1:
                numberx = 10 * i
        for j in range(10):
            if y >= -5+j and y < -5+j+1:
                numbery = j
        for k in range(10):
            if z >= k and z < k+1:
                numberz = 100 * k
        state_number = numberx + numbery +numberz
        state = state_number
        return state













