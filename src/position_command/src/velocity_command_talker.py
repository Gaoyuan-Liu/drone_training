#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist

def position_command_talker():
    pub = rospy.Publisher('/drone_1/cmd_vel', Twist, queue_size=100)
    #pub_2 = rospy.Publisher('/drone_2/command/pose', PoseStamped, queue_size=100)
    rospy.init_node('velocity_command_talker', anonymous=True)
    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        # Conmmand to drone_1
        velocity_command = Twist()
        velocity_command.linear.x = 0
        velocity_command.linear.y = 0
        velocity_command.linear.z = 0.5
        if count > 5:
            if count % 2 != 0:
                velocity_command.linear.z = 0.5
            else:
                velocity_command.linear.z = -0.5
        count = count + 1


        
        #velocity_command.header.frame_id = "drone_1/world"

        pub.publish(velocity_command)


        rate.sleep()

if __name__ == '__main__':
    try:
        position_command_talker()
    except rospy.ROSInterruptException:
        pass
