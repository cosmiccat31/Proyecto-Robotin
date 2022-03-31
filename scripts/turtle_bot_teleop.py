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
    pub = rospy.Publisher('/robot_cmdVel', Twist, queue_size = 10)
    rospy.init_node('turtle_bot_teleop', anonymous = True)
    rate = rospy.Rate(10) # posible cambio
    
    tw = Twist()
    ok = 2
    
    while ok == 2:
        guardar = input("¿Guardar la trayectoria? (Y/N): ")

        if guardar == "Y" or guardar == "y":
            ok = 0
            nombre = input("Nombre de archivo: ")
            file = open("./src/robotin_pkg/results/" + nombre + ".txt", "w")
            print("El archivo ha sido guardado en /src/robotin_pkg/results/" + nombre + ".txt")

        elif (guardar == "N") or (guardar == "n"):
            ok = 1

        else:
            ok = 2

    t = threading.Thread(target = teclado)
    t.start()
    
    print("Ingrese las velocidades:")
    velocidad = float(input("Ingrese Velocidad Lineal: "))
    angulo = float(input("Ingrese Velocidad Angular: "))
    
    if ok == 0:
    	file.write(str(velocidad) + "\n" + str(angulo) + "\n")
    		
    

    while not rospy.is_shutdown():

        if one == "w" and pres == True:
            tw.linear.x = velocidad
            tw.angular.z = 0
            if ok == 0:
                file.write(str(one) + "\n")

        elif one == "s" and pres == True:
            tw.linear.x = -velocidad
            tw.angular.z = 0    
            if ok == 0:
                file.write(str(one) + "\n")

        elif one == "d" and pres == True:
            tw.angular.z = -angulo
            tw.linear.x = 0
            if ok == 0:
                file.write(str(one) + "\n")

        elif one == "a" and pres == True:
            tw.angular.z = angulo
            tw.linear.x = 0
            if ok == 0:
                file.write(str(one) + "\n")

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

    if ok == 0:
        file.close()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

