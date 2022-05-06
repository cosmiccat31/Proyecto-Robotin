#!/usr/bin/env python3
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist
import rospy
import numpy as np

# Consigue las posiciones
def callback(posicion):
    global x, y, z
    x = posicion.x
    y = posicion.y
    z = posicion.z
    
#Se subcribre al topic para obtener la posicion goal
def listener():
    # Se inicia el nodo
    rospy.init_node('robot_manipulador_planner', anonymous=True)
    # Se suscribe al topic robot_manipulator_goal para recibir la posición
    rospy.Subscriber('robot_manipulator_goal', Vector3, callback)
    rospy.spin()

#Publica los angulos para llegar a la posicion
def talker():
    #Se publica los angulos en el topic
    global x,y,z
    theta1 = np.arctan(y/x) #Base phi
    theta2 = np.arctan(z/(np.root(x**2+y**2+z**2)))  #Hombro
    pub = rospy.Publisher('robot_goal', Twist, queue_size = 10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        tw = Twist()
        tw.linear.x = theta2
        tw.linear.y = theta1
        pub.publish(tw)
        rate.sleep()

if __name__ == "__main__":
    try:
        listener()
        talker()
    except rospy.ROSInterruptException:
        pass
