#!/usr/bin/env python3

import gym
import rospy
import time
import numpy as np
import tf
import time
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
    id='QuadcopterLiveShow-v0',
    entry_point='myquadcopter_env:QuadCopterEnv',
    max_episode_steps=30,
    )


class QuadCopterEnv(gym.Env):

    def __init__(self, debug):
        
        # We assume that a ROS node has already been created
        # before initialising the environment
        
        self.vel_pub = rospy.Publisher('/drone_1/cmd_vel', Twist, queue_size=5)
        self.takeoff_pub = rospy.Publisher('/drone_1/takeoff', EmptyTopicMsg, queue_size=0)
        
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
        
        #self.action_space = spaces.Discrete(5) #Forward,Left,Right,Up,Down
        self.num_states = 3
        self.num_actions = 3
        self.reward_range = (-np.inf, np.inf)

        self._seed()

        self.goal_pose = [1, 1, 1]
        self.goal_threshold = 0.05
        self.goal_reward = 50
        self.prev_state = []

    # A function to initialize the random generator
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
        
    # Resets the state of the environment and returns an initial observation.
    def _reset(self):
        
        # 1st: resets the simulation to initial values
        self.gazebo.resetSim()

        # 2nd: Unpauses simulation
        self.gazebo.unpauseSim()

        # 3rd: resets the robot to initial conditions
        self.check_topic_publishers_connection()
        self.init_desired_pose()
        self.takeoff_sequence()

        # 4th: takes an observation of the initial condition of the robot
        data_pose, imu_pose = self.take_observation()
        observation = [data_pose.position.x, data_pose.position.y, data_pose.position.z]
        self.prev_state = observation
        
        # 5th: pauses simulation
        self.gazebo.pauseSim()

        return observation

    def step(self, action):

        # Given the action selected by the learning algorithm,
        # we perform the corresponding movement of the robot

        # 1st, we decide which velocity command corresponds
        vel_cmd = Twist()
        vel_cmd.linear.x = action[0]
        vel_cmd.linear.y = action[1]
        vel_cmd.linear.z = action[2]
        """if action == 0: #FORWARD
            vel_cmd.linear.x = self.speed_value
            vel_cmd.angular.z = 0.0
        elif action == 1: #LEFT
            vel_cmd.linear.x = 0.05
            vel_cmd.angular.z = self.speed_value
        elif action == 2: #RIGHT
            vel_cmd.linear.x = 0.05
            vel_cmd.angular.z = -self.speed_value
        elif action == 3: #Up
            vel_cmd.linear.z = self.speed_value
            vel_cmd.angular.z = 0.0
        elif action == 4: #Down
            vel_cmd.linear.z = -self.speed_value
            vel_cmd.angular.z = 0.0"""

        

        # Then we send the command to the robot and let it go
        # for running_step seconds
        self.gazebo.unpauseSim()
        self.vel_pub.publish(vel_cmd)
        time.sleep(self.running_step)
        data_pose, data_imu = self.take_observation()
        self.gazebo.pauseSim()

        # finally we get an evaluation based on what happened in the sim
        reward,done = self.process_data(data_pose)

        # Promote going forwards instead if turning

        state = [data_pose.position.x, data_pose.position.y, data_pose.position.z]
        self.prev_state = state
        return state, reward, done, {}


    def take_observation (self):
        data_pose = None
        while data_pose is None:
            try:
                data_pose_raw = rospy.wait_for_message('/drone_1/ground_truth_to_tf/pose', PoseStamped, timeout=10)
                data_pose = data_pose_raw.pose # Equals to pose_ in rohit-s-murthy's code
            except:
                rospy.loginfo("Current drone pose not ready yet, retrying for getting robot pose")

        data_imu = None
        while data_imu is None:
            try:
                data_imu = rospy.wait_for_message('/drone_1/raw_imu', Imu, timeout=10)
            except:
                rospy.loginfo("Current drone imu not ready yet, retrying for getting robot imu")
        
        return data_pose, data_imu


    def init_desired_pose(self):
        
        current_init_pose, current_init_imu = self.take_observation()
        
        """self.best_dist = self.calculate_dist_between_two_Points(current_init_pose.position, self.desired_pose.position)"""
    

    def check_topic_publishers_connection(self):
        
        rate = rospy.Rate(10) # 10hz

        while(self.vel_pub.get_num_connections() == 0):
            rospy.loginfo("No susbribers to Cmd_vel yet so we wait and try again")
            rate.sleep();
        rospy.loginfo("Cmd_vel Publisher Connected")
        

    def reset_cmd_vel_commands(self):
        # We send an empty null Twist
        vel_cmd = Twist()
        vel_cmd.linear.z = 0.0
        vel_cmd.angular.z = 0.0
        self.vel_pub.publish(vel_cmd)


    def takeoff_sequence(self, seconds_taking_off=1):
        # Before taking off be sure that cmd_vel value there is is null to avoid drifts
        self.reset_cmd_vel_commands()
        
        takeoff_msg = EmptyTopicMsg()
        rospy.loginfo( "Taking-Off Start")
        self.takeoff_pub.publish(takeoff_msg)
        time.sleep(seconds_taking_off)
        rospy.loginfo( "Taking-Off sequence completed")


    def process_data(self, data_pose):

        done = False
        
        """euler = tf.transformations.euler_from_quaternion([data_imu.orientation.x,data_imu.orientation.y,data_imu.orientation.z,data_imu.orientation.w])
        roll = euler[0]
        pitch = euler[1]
        yaw = euler[2]

        pitch_bad = not(-self.max_incl < pitch < self.max_incl)
        roll_bad = not(-self.max_incl < roll < self.max_incl)
        altitude_bad = data_position.position.z > self.max_altitude

        if altitude_bad or pitch_bad or roll_bad:
            rospy.loginfo ("(Drone flight status is wrong) >>> ("+str(altitude_bad)+","+str(pitch_bad)+","+str(roll_bad)+")")
            done = True
            reward = -200
        else:
            reward, reached_goal = self.get_reward(data_pose)
            if reached_goal:
                print('Reached Goal!')
                done = True"""

        reward, reached_goal = self.get_reward(data_pose)
        if reached_goal:
            print('Reached Goal!')
            done = True  

        return reward,done

    # Now the reward just related to the current_pose and goal
    def get_reward(self, data_pose):
        reward = 0
        reached_goal = False

        error = self._distance(data_pose)
        current_pose = [data_pose.position.x, data_pose.position.y, data_pose.position.z]

        if error < self.goal_threshold:
            reward += self.goal_reward
            reached_goal = True  
        else:
            reward += np.linalg.norm(np.subtract(self.prev_state, self.goal_pose)) - np.linalg.norm(np.subtract(current_pose, self.goal_pose))
        
        return reward, reached_goal

    # Calculate the distance
    def _distance(self, data_pose):
        current_pose = [data_pose.position.x, data_pose.position.y, data_pose.position.z]
        
        err = np.subtract(current_pose, self.goal_pose)
        w = np.array([1, 1, 4])
        err = np.multiply(w,err)
        dist = np.linalg.norm(err)
        return dist






