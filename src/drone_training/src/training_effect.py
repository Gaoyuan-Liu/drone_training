#!/usr/bin/env python

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
import qlearn
import pickle
from gym import wrappers
from geometry_msgs.msg import Pose, PoseStamped
# ROS packages required
import rospy
import rospkg

# import our training environment
import navigation_env_3d

if __name__ == '__main__':
    
    rospy.init_node('drone_gym', anonymous=True)
    #gazebo = GazeboConnection()
    position_pub = rospy.Publisher('/drone/command/pose', PoseStamped, queue_size=100)
    # Create the Gym environment
    env = gym.make('QuadrotorRLControl-v2')
    rospy.loginfo ( "Gym environment done")

    # Get desired position
    desired_position = Pose()
    desired_position.position.z = rospy.get_param("/desired_pose/z")
    desired_position.position.x = rospy.get_param("/desired_pose/x")
    desired_position.position.y = rospy.get_param("/desired_pose/y")

    # Get Q_table
    qtable = {}
    rospack = rospkg.RosPack()
    pkg_path = rospack.get_path('drone_training')
    outdir = pkg_path + '/training_results'
    
    with open(outdir + '/final_Q_table.pkl', 'rb') as f:
        qtable = pickle.load(f)
    



    # They are loaded at runtime by the launch file
    Alpha = rospy.get_param("/alpha")
    Epsilon = rospy.get_param("/epsilon")
    Gamma = rospy.get_param("/gamma")
    #epsilon_discount = rospy.get_param("/epsilon_discount")

    # Initialises the algorithm that we are going to use for learning
    qlearn = qlearn.QLearn(actions=range(env.action_space.n),
                    alpha=Alpha, gamma=Gamma, epsilon=Epsilon)
 

    start_time = time.time()


        
    # Initialization
    current_position = env.take_observation()

    current_command = PoseStamped()
    current_command.pose.position.x = 0.5
    current_command.pose.position.y = 0.5
    current_command.pose.position.z = 5.5
    current_command.header.frame_id = "world"
    position_pub.publish(current_command)
    rospy.loginfo ("")

    # The loop:
    rate = rospy.Rate(100)
    while not env.calculate_state_number(current_position.position.x, current_position.position.y, current_position.position.z) == env.calculate_state_number(desired_position.position.x, desired_position.position.y, desired_position.position.z):
        # Calculate current state
        current_poistion = env.take_observation()
        current_state_observation = [env.calculate_state_number(current_poistion.position.x, current_poistion.position.y, current_poistion.position.z)]
        current_state = ''.join(map(str, current_state_observation))

        # Pick an action based on the current state
        actions = range(7)
        q = [qtable.get((current_state, a), 0.0) for a in actions]        
        maxQ = max(q)
        count = q.count(maxQ)
            # In case there're several state-action max values 
            # we select a random one among them
        if count > 1:
            best = [i for i in range(len(actions)) if q[i] == maxQ]
            i = random.choice(best)
        else:
            i = q.index(maxQ)
        action = actions[i]
##############################################################################
        position_cmd = PoseStamped()
        position_cmd.header.frame_id = "world"
        if action == 0: #FORWARD
            position_cmd.pose.position.x = current_command.pose.position.x + 1
            position_cmd.pose.position.y = current_command.pose.position.y
            position_cmd.pose.position.z = current_command.pose.position.z 
        elif action == 1: #BACKWARD
            position_cmd.pose.position.x = current_command.pose.position.x - 1
            position_cmd.pose.position.y = current_command.pose.position.y
            position_cmd.pose.position.z = current_command.pose.position.z
        elif action == 2: #RIGHT
            position_cmd.pose.position.x = current_command.pose.position.x
            position_cmd.pose.position.y = current_command.pose.position.y + 1
            position_cmd.pose.position.z = current_command.pose.position.z
        elif action == 3: #LEFT
            position_cmd.pose.position.x = current_command.pose.position.x
            position_cmd.pose.position.y = current_command.pose.position.y - 1
            position_cmd.pose.position.z = current_command.pose.position.z
        elif action == 4: #UP
            position_cmd.pose.position.x = current_command.pose.position.x 
            position_cmd.pose.position.y = current_command.pose.position.y
            position_cmd.pose.position.z = current_command.pose.position.z + 1
        elif action == 5: #DOWN
            position_cmd.pose.position.x = current_command.pose.position.x 
            position_cmd.pose.position.y = current_command.pose.position.y
            position_cmd.pose.position.z = current_command.pose.position.z - 1
        elif action == 6: #still
            position_cmd.pose.position.x = current_command.pose.position.x 
            position_cmd.pose.position.y = current_command.pose.position.y
            position_cmd.pose.position.z = current_command.pose.position.z
        
        if position_cmd.pose.position.z < 0:
            position_cmd.pose.position.z = 0.4
###############################################################################       
        
        position_pub.publish(position_cmd)
        data_pose = env.take_observation()
        current_position = data_pose
        current_command = position_cmd
        rate = rospy.Rate(100)
        while not env.calculate_state_number(current_position.position.x, current_position.position.y, current_position.position.z) == env.calculate_state_number(position_cmd.pose.position.x, position_cmd.pose.position.y, position_cmd.pose.position.z):
            position_pub.publish(position_cmd)
            current_position = env.take_observation()
            rate.sleep()
        rate.sleep()

    
    position_pub.publish(current_command)
    rospy.loginfo ("ARRIVED!")

####################################
    env.close()




