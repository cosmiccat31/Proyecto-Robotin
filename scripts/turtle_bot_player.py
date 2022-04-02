#!/usr/bin/env python3
from geometry_msgs.msg import Twist
import rospy
from tkinter import filedialog
from tkinter import *
from pynput.keyboard import Key, Listener
global tw, one, pres, guardar, count, file_name


# Function for opening the
# file explorer window


def browseFiles():
  ftypes = [("Text files", "*.txt"), ("all files", "*.*")]
  file = filedialog.askopenfilename(initialdir = "./src/turtle_bot_10/results/",title = "Select a File",filetypes = ftypes)
  return file

# Collect events until released
def talker():
    global tw, one, pres, guardar, count, file_name
    # Creación del nodo y el topic
    pub = rospy.Publisher('/turtlebot_cmdVel', Twist, queue_size=10)
    rospy.init_node('turtle_bot_player', anonymous=True)
    rate = rospy.Rate(10)

    file_name = browseFiles()
    file = open(file_name, "r")
    Lines = file.readlines()
    tw = Twist()

    velocidad = float(Lines[0])
    angulo = float(Lines[1])

    #print("Por favor no presionar ninguna tecla \n")
    print(velocidad, angulo)
    
    # Loop principal
    while not rospy.is_shutdown():
        for i in range(2,len(Lines)+1):
            one = Lines[i]
            one = one[0]
            print(one)
            
            if i == len(Lines)-1:
                one = "p"

            if one == "w":
                tw.linear.x = velocidad
                tw.angular.z = 0

            elif one == "s":
                tw.linear.x = -velocidad
                tw.angular.z = 0

            elif one == "d":
                tw.angular.z = -angulo
                tw.linear.x = 0

            elif one == "a":
                tw.angular.z = angulo
                tw.linear.x = 0

            elif one == "p":
                tw.linear.x = 0
                tw.linear.y = 0
                tw.linear.z = 0
                tw.angular.x = 0
                tw.angular.y = 0
                tw.angular.z = 0

            else:
                tw.linear.x = 0
                tw.linear.y = 0
                tw.linear.z = 0
                tw.angular.x = 0
                tw.angular.y = 0
                tw.angular.z = 0
                
            pub.publish(tw)
            rate.sleep()

    file.close()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass	
