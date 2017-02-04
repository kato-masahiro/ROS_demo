#!/usr/bin/env python
#encode:UTF-8

import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

rospy.init_node("vel_1umper")

#速度をパラメータでセットする
vel_x = rospy.get_param("~vel_x",0.5)
vel_rot = rospy.get_param("~vel_rot",1.0)

pub = rospy.Publisher("/mobile_base/commands/velocity",Twist,queue_size=10)

def callback(bumper):
    print bumper
    vel = Twist()
    vel.linear.x = -1.0
    pub.publish(vel)

sub = rospy.Subscriber("/mobile_base/events/bumper",BumperEvent,callback)

while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input("f:forward,b:backward,l:left,r:right >>")
    if "f" in direction:
        vel.linear.x = 0.5
    if "b" in direction:
        vel.linear.x = -0.5
    if "r" in direction:
        vel.angular.z = 1.0
    if "l" in direction:
        vel.angular.z = -1.0
    if "q" in direction:
        break
    print vel
    pub.publish(vel)
