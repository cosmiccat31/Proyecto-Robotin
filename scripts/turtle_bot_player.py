#!/usr/bin/env python3
import rospy
import threading
from pynput.keyboard import Key, Listener
from geometry_msgs.msg import Twist

# from turtle_bot_10.srv import reproduccion, reproduccionResponse
global tw, one, pres, guardar, count, file_name


def handle_reproduccion(req):
    print("Returning[%s]" % (req.trayectoria))

    return req.trayectoria


# Collect events until released
def talker():
    global tw, one, pres, guardar, count, file_name
    pub = rospy.Publisher('/robot_cmdVel', Twist, queue_size=10)
    rospy.init_node('turtle_bot_player', anonymous=True)
    rate = rospy.Rate(10)  # posible cambio

    file_name = input("Nombre del archivo: ")
    # file_name = rospy.Service('reproduccion', reproduccion,handle_reproduccion)
    file = open("./src/robotin_pkg/results/" + str(file_name) + ".txt", "r")
    tw = Twist()

    # file = open("./src/turtle_bot_10/results/" + file_name + ".txt", "r")
    Lines = file.readlines()

    # t = threading.Thread(target = teclado)
    # t.start()

    velocidad = float(Lines[0])
    angulo = float(Lines[1])

    print("Por favor no presionar ninguna tecla \n")
    print(velocidad, angulo)

    while not rospy.is_shutdown():
        for i in range(2,len(Lines)+1):
            one = Lines[i]
            one = one[0]
            print(one)

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

            # pres = True
            pub.publish(tw)
            rate.sleep()

    file.close()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
