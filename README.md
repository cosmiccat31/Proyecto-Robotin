# Taller-2  Robotin 🤖
En este repositorio se presenta la implementación de un robot diferencial.

## Introducción
### Primeros pasos
1. Instalar rosserial y la libreria ros_lib en arduino, seguir el siguiente tutorial: [ROSSERIAL](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup).
2. Correr roscore.
3. Correr rosrun rosserial_python serial_node.py /dev/ttyACM0 para establecer la conexión con el arduino.
4. Ir al workspace cd robot_ws
5. Hacer source devel/setup.bash

NOTA: Todos los nodos se encuentran en el paquete robotin_pkg
### Punto 1: --------------- ⌨️ OPERAR EL TURTLEBOT🐢️ MEDIANTE EL TECLADO ⌨️ ---------------
* Cargar el archivo (teleop_arduino) al arduino 
* Correr rosrun rosserial_python serial_node.py /dev/ttyACM0
* Correr rosrun robotin_pkg turtebot_teleop.py
* Al momento de correrlo, se solicitará si desea guardar el archivo con las trayectorias. Si selecciona "Y" este le solicitará un nombre para el archivo, el cual se guardará en la carpeta "talleres_ws/src/turtle_bot_10/results/", si selecciona "N", no se guardarán las trayectorias. En ambos casos se solicitará la velocidad lineal y angular para TurtleBot (Se recomiendan 70 y 180 respectivamente).

CONFIGURACIÓN DE TECLADO PARA TURTLEBOT:

                         W   ADELANTE
               
   IZQUIERDA <---- A     S     D  ----> DERECHA
                         |
                         |
                       ATRÁS
                       
