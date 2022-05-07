#!/usr/bin/env python3
import tkinter as tk
from geometry_msgs.msg import Twist
import rospy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.filedialog import *

class VentanaSeñales(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        #Definición de la interfaz
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.frame_graficas = tk.Frame(self, bg="#6E6E6E")
        #self._figure_1, self._ax1 = plt.subplots()
        self.figure1 = plt.figure()
        self.ax1 = self.figure1.add_subplot(111, projection='3d')
        self._figure_1_canvas = FigureCanvasTkAgg(self.figure1, master=self.frame_graficas)
     
        self.frame_graficas.grid_columnconfigure(0, weight=1, uniform="fig")
        self._figure_1_canvas.get_tk_widget().grid(row=0, column=0, padx=(10, 30), pady=(30, 30),sticky="nsew")

        self.frame_botones = tk.Frame(self)
        #Definición de los botones
        self.btn_guardar = tk.Button(self.frame_botones,font=('Courier', 16),text="Guardar", command=self.guardar)

        #Ubicación de los botones    
        self.btn_guardar.pack(side="bottom")

        self._anim1 = None

        self.frame_graficas.pack(fill="both")
        self.frame_botones.pack(fill="x")
        self._init_axes()


        global x,y,z
        x = []
        y = []
        z = []

        #Consige las posiciones
        def callback(data):
            global x, y, z
	     # geometria de la garra
	     # velocidades angulares de las ruedas
            theta=data.linear.x
            phi=data.linear.y
            r=data.angular.z

            x.append(r*np.sin(theta)*np.cos(phi))
            y.append(r*np.sin(theta)*np.sin(phi))
            z.append(r*np.cos(theta))
             
        #Se inicia el nodo
        rospy.init_node('robot_manipulador_interface', anonymous = True)
        #Se suscribe al topic turtlebot_position para consegir la posición actual del robot
        rospy.Subscriber('robot_angulo', Twist, callback)
        
        #Se encarga de graficar las posiciones
        def func_animation(i):
             global x,y,z
             self.ax1.plot(x,y,z)
	
        if self._anim1 is None:
        
            self.anim = animation.FuncAnimation(self.figure1, func_animation, 100)
            self._figure_1_canvas.draw()
         
        else:
            self._ax1.lines = []  
            self._anim1 = None

    def _init_axes(self):

        self.ax1.set_title('Posición del Robot')
        self.ax1.set_xlabel("x")
        self.ax1.set_ylabel("y")
        self.ax1.set_zlabel("z")
        self.ax1.set_xlim(-16, 16)
        self.ax1.set_ylim(-16, 16)
        self.ax1.set_zlim(-1, 16)

    
    #Boton guardar grafica
    def guardar(self):
        if self.btn_guardar["text"] == "Guardar":
                      
            input_path = asksaveasfilename()
            plt.savefig(input_path)
            #inputpath1 = input_path.set(input_path)
            #print(input_path)
        else:
            #self._anim1.event_source.start()
            self.btn_guardar.configure(text="Guardado")

if __name__ == "__main__":
    root = tk.Tk()
    VentanaSeñales(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
