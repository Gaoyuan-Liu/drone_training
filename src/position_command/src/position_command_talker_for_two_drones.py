#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def position_command_talker():
    pub_1 = rospy.Publisher('/drone_1/command/pose', PoseStamped, queue_size=100)
    pub_2 = rospy.Publisher('/drone_2/command/pose', PoseStamped, queue_size=100)
    rospy.init_node('position_command_talker', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        # Conmmand to drone_1
        position_command_1 = PoseStamped()
        position_command_1.pose.position.x = 3
        position_command_1.pose.position.y = 3
        position_command_1.pose.position.z = 3
        position_command_1.header.frame_id = "drone_1/world"
        # Conmmand to drone_2
        position_command_2 = PoseStamped()
        position_command_2.pose.position.x = 3
        position_command_2.pose.position.y = 3
        position_command_2.pose.position.z = 3
        position_command_2.header.frame_id = "drone_2/world"

        pub_1.publish(position_command_1)
        pub_2.publish(position_command_2)

        rate.sleep()

if __name__ == '__main__':
    try:
        position_command_talker()
    except rospy.ROSInterruptException:
        pass
