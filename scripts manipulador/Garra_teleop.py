#!/usr/bin/env python3
import rospy
import threading
from pynput.keyboard import Key, Listener
from geometry_msgs.msg import Twist
global tw, one, pres, ok,guardar

def on_press(key):
    global tw, one, pres
    try:
        # print('alphanumeric key {0} pressed'.format(key.char))
        one = key.char
        pres = True

    except AttributeError:
        pass
        # print('special key {0} pressed'.format(key))

def on_release(key):
    global pres
    pres = False

    # print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
def teclado():
    with Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

def talker():
    global tw, one, pres, ok,guardar
    pub = rospy.Publisher('/robot_pinza', Twist, queue_size = 10)
    rospy.init_node('robot_manipulador_teleop', anonymous = True)
    rate = rospy.Rate(10) 
    
    tw = Twist()
    ok = 2
    

    t = threading.Thread(target = teclado)
    t.start()
    
    print("Ingrese las velocidades:")
    hombro = float(input("Ingrese la velocidad del hombro: "))
    base = float(input("Ingrese la velocidad de la base: "))
    garra = float(input("Ingrese la velocidad de la garra: ")) #La unica que sirve
    
    while not rospy.is_shutdown():


      #Servo1 homrbo
        if one == "e" and pres == True:
            tw.linear.y = garra       

        elif one == "r" and pres == True:
            tw.linear.y = -garra

         # Servo 3  Garra rr
        elif one == "u" and pres == True:
            tw.linear.z = -garra

        elif one == "i" and pres == True:
            tw.linear.z = garra
            
        elif one == "y" and pres == True:
            tw.linear.x = garra
            
        elif one == "t" and pres == True:
            tw.linear.x = -garra
            
        elif one == "p" and pres == False:
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

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
