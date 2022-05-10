# Taller  Robotin 🤖
En este repositorio se presenta la implementación de un robot diferencial.

## Introducción
### Primeros pasos
1. Instalar rosserial y la libreria ros_lib en arduino, seguir el siguiente tutorial: [ROSSERIAL](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup).
2. Correr: `roscore`
3. Correr: `rosrun rosserial_python serial_node.py /dev/ttyACM0` para establecer la conexión con el arduino.
4. Ir al workspace: `cd robot_ws && source devel/setup.bash`

NOTA: Todos los nodos se encuentran en el paquete robotin_pkg
## INFORMACION GENERAL DEL ROBOT
# Lista de materiales

* Puente H: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiszoDG4_X2AhVQTDABHfdMA3kQFnoECAMQAQ&url=https%3A%2F%2Fnaylampmechatronics.com%2Fdrivers%2F11-driver-puente-h-l298n.html&usg=AOvVaw1h8v7_93jsQKV1_FgbscjP
* Raspberry pi 4: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiggYXU4_X2AhVsSzABHbPyAPoQFnoECAYQAQ&url=https%3A%2F%2Fstatic.raspberrypi.org%2Ffiles%2Fproduct-briefs%2FRaspberry-Pi-4-Product-Brief.pdf&usg=AOvVaw3kKN1og-Ib_H0iYch2ncAj
* Arduino uno: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjQ17Tc4_X2AhUvSTABHbBRCrgQFnoECAIQAQ&url=https%3A%2F%2Fwww.farnell.com%2Fdatasheets%2F1682209.pdf&usg=AOvVaw2hpzYjytzW3E48klQUKjqJ
* Regulador de voltaje: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj7ioD44_X2AhWsSjABHbafDoEQFnoECA4QAQ&url=https%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Flm2596&usg=AOvVaw2hyIUL8FdL0D7XjtzvMXII

## Punto 1  ⌨️ OPERAR EL TURTLEBOT🐢️ MEDIANTE EL TECLADO ⌨️ 
* Cargar el archivo (teleop_arduino) al arduino 
* Correr rosrun rosserial_python serial_node.py /dev/ttyACM0
* Correr rosrun robotin_pkg turtebot_teleop.py
* Al momento de correrlo, se solicitará si desea guardar el archivo con las trayectorias. Si selecciona "Y" este le solicitará un nombre para el archivo, el cual se guardará en la carpeta "talleres_ws/src/turtle_bot_10/results/", si selecciona "N", no se guardarán las trayectorias. En ambos casos se solicitará la velocidad lineal y angular para TurtleBot.

## Punto 2  📈️ GRAFICAR LA TRAYECTORIA QUE RECORRE TURTLEBOOT🐢️ 📈️ 

1. Correr "⌨️ OPERAR EL TURTLEBOT🐢️ MEDIANTE EL TECLADO ⌨️" (El usuario decide si quiere guardar el recorrido o no).
2. Abrir un nuevo terminal y entrar a la carpeta "robot_ws" con el código:     cd robot_ws/
3. Realizar un setup.bash con el siguiente código:     source devel/setup.bash
4. Correr el .py "turtle_bot_interface" con el siguiente código:     rosrun robotin_pkg turtle_bot_interface.py

Se desplegará una interfaz que contendrá una gráfica y un botón. La gráfica se actualizará en tiempo real a medida que el usuario mueva al TurtleBot en el mapa. Si el usuario desea guardar dicha gráfica, debe dar click en el botón GUARDAR, el cual le solicitará la carpeta en donde deseará guardar la gráfica. Esta se guardará en .png


## Punto 4  🚶️ REPLICAR LA UNA TRAYECTORIA YA DEFINIDA CON TURTLEBOT🐢️ 🚶️ 

*NO DEBE CORRER PREVIAMENTE "⌨️ OPERAR EL TURTLEBOT🐢️ MEDIANTE EL TECLADO ⌨️" YA QUE PUEDE ALTERAR LA TRAYECTORIA DEFINIDA DE TURTLEBOT.

1. Abrir un nuevo terminal y entrar a la carpeta "robot_ws" con el código:     cd robot_ws/
2. Realizar un setup.bash con el siguiente código:     source devel/setup.bash
3. Correr el .py "turtle_bot_interface" con el siguiente código:     rosrun robotin_pkg turtle_bot_player.py

Se solicitará el nombre del archivo de texto .txt donde se contienen las velocidades y la trayectoria. El archivo .txt será buscado en la carpeta "robot_ws/src/robotin_pkg/results/", por lo que previamente deberá ser ubicado en ese directorio. Una vez el usuario escriba el nombre del archivo de texto (SIN .txt), Turtlebot replicará el recorrido allí contenido.

                      
