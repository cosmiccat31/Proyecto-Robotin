#!/usr/bin/env python3
import tkinter as tk
from geometry_msgs.msg import Twist
import rospy
import matplotlib.pyplot as plt
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
        self._figure_1, self._ax1 = plt.subplots()
        self._figure_1_canvas = FigureCanvasTkAgg(self._figure_1, master=self.frame_graficas)
     
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


        global x,y
        x = []
        y = []
	theta = [np.pi/2]

        #Consige las posiciones
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
             
        #Se inicia el nodo
        rospy.init_node('turtle_bot_interface', anonymous = True)
        #Se suscribe al topic turtlebot_position para consegir la posición actual del robot
        rospy.Subscriber('robot_cmdVel', Twist, callback)
        
        #Se encarga de graficar las posiciones
        def func_animation(i):
             global x,y
             plt.plot(x,y)
	
        if self._anim1 is None:
        
            self.anim = animation.FuncAnimation(self._figure_1, func_animation, 100)
            self._figure_1_canvas.draw()
         
        else:
            self._ax1.lines = []  
            self._anim1 = None

    def _init_axes(self):

        self._ax1.set_title('Posición del Robot')
        self._ax1.set_xlabel("x")
        self._ax1.set_ylabel("y")
        self._ax1.set_xlim(-2.5, 2.5)
        self._ax1.set_ylim(-2.5, 2.5)

    
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
