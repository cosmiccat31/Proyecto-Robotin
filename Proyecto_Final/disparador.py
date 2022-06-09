#!/usr/bin/env python3
import rospy
import threading
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys


def talker():
    global ordenesLista
    pub = rospy.Publisher('direcciones', String, queue_size = 10)
    rospy.init_node('disparador', anonymous = True)
    rate = rospy.Rate(1)
    
    mensaje = String()
    orientacion=0
    ordenesLista=[]
    while not rospy.is_shutdown():
        

        mensaje = 'disparar'
        #rospy.loginfo(mensaje)
        #rate.sleep()
        pub.publish(mensaje)
        #rate.sleep()
        rate.sleep()  
        mensaje = 'disparar'
        #rospy.loginfo(mensaje)
        #rate.sleep()
        pub.publish(mensaje)
        sys.exit()
        
        # pub.publish(mensaje)
        # rate.sleep()        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
        pass
