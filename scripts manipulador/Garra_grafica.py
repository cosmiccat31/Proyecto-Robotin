#!/usr/bin/env python3
import tkinter as tk
from geometry_msgs.msg import Twist
import rospy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.filedialog import *
import threading

#figure, axis = plt.subplots()

global x,y,z
x=[]
y=[]
z=[]

fig=plt.figure('Trayectoria')
ax=fig.gca(projection='3d')

#Consigue las posiciones
def callback(data):
    global x,y,z
    theta=data.linear.x
    phi=data.linear.y
    r=data.angular.z
    x.append(r*np.sin(theta)*np.cos(phi))
    y.append(r*np.sin(theta)*np.sin(phi))
    z.append(r*np.cos(theta))

def map():
	
	mp = animation.FuncAnimation(plt.gcf(), graph, 10000)
	plt.show()

def grafica():
    #Se inicia el nodo
    rospy.init_node('robot_manipulador_interface', anonymous = True)
    #Se suscribe al topic turtlebot_position para consegir la posición actual del robot
    rospy.Subscriber('robot_angulo', Twist, callback)
    t = threading.Thread(target = map)
    t.start()

def graph(i):
    global x,y,z
    ax.cla()
    ax.plot(x,y,z,'r--')
    ax.set_title('Posición del Robot')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-16, 16)
    ax.set_ylim(-16, 16)
    ax.set_zlim(-1, 16)

#Se encarga de graficar las posiciones
# def func_animation(i):
#     global x,y
#     plt.plot(x,y,z)

# baboni = animation.FuncAnimation(figure, func_animation, 100)
# ax.set_title('Posición del Robot')
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_xlim(-16, 16)
# ax.set_ylim(-16, 16)






# fig=plt.figure('Trayectoria')
# ax=fig.gca(projection='3d')

# ax.plot(x,y,z,'r.')
# plt.show()

if __name__ == "__main__":
    try:
        grafica()
    except rospy.ROSInterruptException: pass
