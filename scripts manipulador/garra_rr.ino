#include <Servo.h>
#include <ros.h>
#include <geometry_msgs/Twist.h>

Servo Servo1; //Hombro            
Servo Servo2; //Base
Servo Servo3; //Garra 

int Hombro; 
int Base; 
int Garra;        //Variable que guarda el valor de la velocidad lineal

int posH=0;
int posB=0;
int posG=0;

ros::NodeHandle  nh;
geometry_msgs::Twist tw_msg;

void messageCb( const geometry_msgs::Twist& robot_pinza){
  Hombro = robot_pinza.linear.x;
  Base = robot_pinza.linear.y;
  Garra = robot_pinza.linear.z;
  
 //Abrir
  if(Garra>0){
  Servo3.write(180);  
  }
  //Cerrar
  if(Garra<0){
  Servo3.write(0);
  }

  //Subir
  if (Base>0) { //if Value read of the button ==LOW:
    posB=posB+5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    delay(5); //5 milliseconds of delay
    Servo2.write(posB); //servo goes to variable pos
    
  }
  //Bajar
  if(Base<0) { //if Value read of the button ==LOW:
    posB=posB-5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    delay(5); //5 milliseconds of delay
    Servo2.write(posB); //servo goes to variable pos
  }

  //Izquierda
  if (Hombro>0) { //if Value read of the button ==LOW:
    posH=posH+5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    delay(5); //5 milliseconds of delay
    Servo1.write(posH); //servo goes to variable pos
    
  }
  //Derecha
  if(Hombro<0) { //if Value read of the button ==LOW:
    posH=posH-5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    delay(5); //5 milliseconds of delay
    Servo1.write(posH); //servo goes to variable pos
  }
}

ros::Subscriber<geometry_msgs::Twist> sub("robot_pinza", &messageCb ); //Se suscribe al topic robot_cmdVel para recibir las velocidades

void setup()
{   
  // Define the servo signal pins
  Servo1.attach (10); //Hombro      
  Servo2.attach (9); //Base
  Servo3.attach (3); //Garra rr
  // Posiciones iniciales
  Servo1.write(90);
  Servo2.write(80);
  Servo3.write(180);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
