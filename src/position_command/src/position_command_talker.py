#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def position_command_talker():
    pub = rospy.Publisher('/drone/command/pose', PoseStamped, queue_size=100)
    rospy.init_node('position_command_talker', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        position_command = PoseStamped()
        position_command.pose.position.x = 3
        position_command.pose.position.y = 3
        position_command.pose.position.z = 3
        position_command.header.frame_id = "world"
        pub.publish(position_command)
        rate.sleep()

if __name__ == '__main__':
    try:
        position_command_talker()
    except rospy.ROSInterruptException:
        pass
