#!/usr/bin/env python3
import rospy
import threading
from geometry_msgs.msg import Twist
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

global x,y,theta

x = [0]
y = [0]
theta = [np.pi/2]

def grafica():

	rospy.init_node('turtle_bot_position', anonymous = True)
	rospy.Subscriber('robot_cmdVel', Twist, callback)

	t = threading.Thread(target = mapa)
	t.start()


def callback(data):
	global x, y, theta
	
	# geometria del robot
	rw = 2
	l = 8
	# velocidades angulares de las ruedas
	R = np.array([[np.cos(theta[-1]), -np.sin(theta[-1]), 0],
				  [np.sin(theta[-1]), np.cos(theta[-1]), 0],
				  [0, 0, 1]])
	dx = data.linear.x
	dy = data.linear.y
	dw = data.angular.z

	ZR = np.array([dx, dy, dw])
	ZI = np.dot(R, ZR)

	dt = 0.1
	dtt=0.033
	x.append(x[-1] + np.dot(dt, ZI[0]))
	y.append(y[-1] + np.dot(dt, ZI[1]))
	theta.append(theta[-1] + np.dot(dtt, ZI[2]))


def mapa():

	camilo = animation.FuncAnimation(plt.gcf(), dibujo, 10000)
	plt.show()


def dibujo(i):
	global x,y

	plt.cla()
	plt.plot(x,y)
	plt.xlim([-250, 250])
	plt.ylim([-250, 250])
	plt.xlabel('Posición eje X')
	plt.ylabel('Posición eje Y')
	plt.title('Ubicación en tiempo real del Robot')
	#plt.savefig("./src/turtle_bot_11/results/trayectoria_punto2.png")

if __name__ == '__main__':
    try:
        grafica()
    except rospy.ROSInterruptException: pass
