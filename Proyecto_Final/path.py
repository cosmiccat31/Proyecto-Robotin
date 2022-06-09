#!/usr/bin/env python3
import rospy
import threading
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys

from cmath import pi
from implementation import *

diagram3 = GridWithWeights(13, 43)
diagram3.walls = [(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(12,9),(13,9),(5,10),(6,10),(7,10),(8,10),(9,10),(10,10),(11,10),(12,10),(13,10),
                  (5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11),(12,11),(13,11),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(12,12),(13,12),
                  
                  (0,16),(0,17),(0,18),(1,16),(1,17),(1,18),(2,16),(3,16),(4,16),(2,17),(3,17),(4,17),(2,18),(3,18),(4,18),
                  
                  #(0,20),(1,20),(2,20),(3,20),(0,21),(1,21),(2,21),(3,21),(0,22),(1,22),(2,22),(3,22),(0,23),(1,23),(2,23),(3,23),#inicio
                  
                  (10,16),(11,16),(12,16),(10,17),(11,17),(12,17),(10,18),(11,18),(12,18),
                  
                  (5,24),(6,24),(7,24),(8,24),(9,24),(5,25),(6,25),(7,25),(8,25),(9,25),(5,26),(6,26),(7,26),(8,26),(9,26),(5,27),(6,27),(7,27),(8,27),(9,27),
                  
                  (10,29),(11,29),(12,29),(10,30),(11,30),(12,30),(10,31),(11,31),(12,31),(10,32),(11,32),(12,32),
                  
                  (0,33),(1,33),(2,33),(3,33),(4,33),(5,33),(6,33),(0,34),(1,34),(2,34),(3,34),(4,34),(5,34),(6,34),
                  (0,35),(1,35),(2,35),(3,35),(4,35),(5,35),(6,35),(0,36),(1,36),(2,36),(3,36),(4,36),(5,36),(6,36)]
#draw_grid(diagram3, number=diagram3.weights)

# start, goal = (0, 21), (3, 39) #------------------------------------------PUNTOS INICIIO Y FIINAL---------------------------------------

# came_from, cost_so_far = dijkstra_search(diagram3, start, goal)
# #draw_grid(diagram3, point_to=came_from, start=start, goal=goal)
# print()
# draw_grid(diagram3, path=reconstruct_path(came_from, start=start, goal=goal))
# camino = reconstruct_path(came_from, start=start, goal=goal)
# print(camino)

# #draw_grid(diagram3, number=cost_so_far, start=start, goal=goal)

def ordenes(p1,p2,orientacion):
    #orientacion=0
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    pi=180
    orden=[]
    
    if orientacion==0:
        #arriba
        if dx==0 and dy>0:
            orden = ['izquierda','adelante']
            orientacion = pi/2
        #abajo
        if dx==0 and dy<0:
            orden = ['derecha','adelante']
            orientacion = -pi/2
        #izquierda
        if dx>0 and dy==0:
            orden = ['izquierda','izquierda','adelante']
            orientacion = pi
        #derecha
        if dx<0 and dy==0:
            orden = ['adelante']
            orientacion = 0
        return [orden,orientacion]
    if orientacion==pi/2:
        #arriba
        if dx==0 and dy>0:
            orden = ['adelante']
            orientacion = pi/2
        #abajo
        if dx==0 and dy<0:
            orden = ['derecha','derecha','adelante']
            orientacion = -pi/2
        #izquierda
        if dx>0 and dy==0:
            orden = ['izquierda','adelante']
            orientacion = pi
        #derecha
        if dx<0 and dy==0:
            orden = ['derecha','adelante']
            orientacion = 0
        return [orden,orientacion]
    if orientacion==-pi/2:
        #arriba
        if dx==0 and dy>0:
            orden = ['izquierda','izquierda','adelante']
            orientacion = pi/2
        #abajo
        if dx==0 and dy<0:
            orden = ['adelante']
            orientacion = -pi/2
        #izquierda
        if dx>0 and dy==0:
            orden = ['derecha','adelante']
            orientacion = pi
        #derecha
        if dx<0 and dy==0:
            orden = ['izquierda','adelante']
            orientacion = 0
        return [orden,orientacion]
    if orientacion==pi:
        #arriba
        if dx==0 and dy>0:
            orden = ['derecha','adelante']
            orientacion = pi/2
        #abajo
        if dx==0 and dy<0:
            orden = ['izquierda','adelante']
            orientacion = -pi/2
        #izquierda
        if dx>0 and dy==0:
            orden = ['adelante']
            orientacion = pi
        #derecha
        if dx<0 and dy==0:
            orden = ['izquierda','izquierda','adelante']
            orientacion = 0
        return [orden,orientacion]
#--------------------------------------------------------------------------FUNCIÓN QUE PIDE PUNTOS------------------
def listaPasos():
    #Toma de valores
    goal = (0,0)
    start = (0,21)
    orientacion = 0
    ordenesLista=[]
    start, goal = (0, 21), (3, 39)
    print('Ingresar punto de inicio(0,21 por defecto)')
    xi = int(input('x:'))
    yi = int(input('y:'))
    start = (xi,yi)
    print(start)
    print('Ingresar punto destino')
    xg = int(input('x:'))
    yg = int(input('y:'))
    goal = (xg,yg)
    print(goal)
    #Implementación de path planning
    came_from, cost_so_far = dijkstra_search(diagram3, start, goal)
    print()
    draw_grid(diagram3, path=reconstruct_path(came_from, start=start, goal=goal))
    camino = reconstruct_path(came_from, start=start, goal=goal)
    #print(camino)
    return camino

def talker():
    global ordenesLista
    pub = rospy.Publisher('direcciones', String, queue_size = 10)
    rospy.init_node('path', anonymous = True)
    rate = rospy.Rate(0.85)
    
    mensaje = String()
    orientacion=0
    ordenesLista=[]
    while not rospy.is_shutdown():
        
        camino = listaPasos()
        for i in range(len(camino)):
            try:
                orden,orientacion=ordenes(camino[i],camino[i+1],orientacion)
                ordenesLista = ordenesLista + orden
                ordenesLista.append('a')

            except:
                print('PARAR')
        #print(ordenesLista)s
        ordenesLista.append('detente por favor')
        for j in range(len(ordenesLista)):
            mensaje = ordenesLista[j]
            #rospy.loginfo(mensaje)
            rate.sleep()
            pub.publish(mensaje)
            #rate.sleep()
            
        if j == len(ordenesLista)-1:
            sys.exit()
        
        # pub.publish(mensaje)
        # rate.sleep()        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
        pass