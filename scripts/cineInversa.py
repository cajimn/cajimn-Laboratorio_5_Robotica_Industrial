from cmath import acos, asin, atan, pi, sin, sqrt

from matplotlib.lines import Line2D
import rospy
import time
import numpy as np
import math as m
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = pose(10.0,10.0,10.0,False)
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = pose(10.0,10.0,10.0,False)
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def pose(x,y,z,grip):
    h=14
    L1=10.6
    L2=10.6
    L3=11
    L4=90.0
    th=[0.0,0.0,0.0,0.0,0.0]
    if x == 0.0:
        x = 0.001

    th[0]=m.atan(y/x)
    R1 = m.sqrt(pow(x, 2) + pow(y, 2))
    zm = z - h
    R2 = R1 - L3
    th[2]=m.acos((pow(R2, 2) + pow(zm, 2) - pow(L1, 2) - pow(L2, 2)) / (2*L1*L2))
    th[1]=m.atan(R2 / zm)
    th[3]=-(m.pi / 2) + abs(th[1]) + abs(th[2])
    
    if grip:
        th[4]=5
    else: 
        th[4]=0

    #p = directa(th)
    #print(p)
    return th

def directa(th):

    L1=100.0
    L2=105.0
    L3=97.0
    L4=90.0
    
    alpha=73.4*pi/180 


    H = L2*m.cos(th[1]+alpha)+L3*m.cos(th[1]+th[2])+L4*m.cos(th[1]+th[2]+th[3])
    
    x = H*m.cos(th[0])
    y = H*m.sin(th[0])
    z = L2*m.sin(th[1]+alpha)+L3*m.sin(th[1]+th[2])+L4*m.sin(th[1]+th[2]+th[3])+L1
    
    return [x,y,z]

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass

