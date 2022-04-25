/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */
/*
 *             LIBRERIAS
 */
#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <AFMotor.h>
#include<math.h>
/*
 *        Definición de Variables
 */
AF_DCMotor Motor1(2); //Motor Izquierdo
AF_DCMotor Motor2(3); //Motor Derecho
int VelLinear;        //Variable que guarda el valor de la velocidad lineal
int VelAngular;       //Variable que guarda el valor de la velocidad angular
int M;

ros::NodeHandle  nh;
geometry_msgs::Twist tw_msg;
ros::Publisher Position("robot_position", &tw_msg);

/*
 * messageCb: Recibe los valores publicados en el topic robot_cmdVel
 */
void messageCb( const geometry_msgs::Twist& robot_cmdVel){
  //Se traduce la velocidad lineal y angular en PWM
  VelLinear = round(robot_cmdVel.linear.x/59.56*255);
  VelAngular = round(robot_cmdVel.angular.z/14.88*255);
  M = 2.12;
  //Adelante
  if(VelLinear>0){
  Motor1.setSpeed(VelLinear-M);
  Motor2.setSpeed(VelLinear);
  Motor1.run(FORWARD);
  Motor2.run(FORWARD);
  }
  
  //Atras
  if (VelLinear<0){
  Motor1.setSpeed(VelLinear*-1-M);
  Motor2.setSpeed(VelLinear*-1);
  Motor1.run(BACKWARD);
  Motor2.run(BACKWARD);
  }
  
 //Izquierda
  if(VelAngular>0){
   
  Motor1.setSpeed(VelAngular);
  Motor2.setSpeed(VelAngular);
  Motor1.run(BACKWARD);
  Motor2.run(FORWARD);
  }
  
  //Derecha
  if(VelAngular<0){
 
  Motor1.setSpeed(VelAngular*-1);
  Motor2.setSpeed(VelAngular*-1);
  Motor1.run(FORWARD);
  Motor2.run(BACKWARD);
  }
  
  //Stop
  if(VelLinear==0&&VelAngular==0){
  Motor1.setSpeed(0);
  Motor2.setSpeed(0);
  Motor1.run(RELEASE);
  Motor2.run(RELEASE);
  }  
   
}

ros::Subscriber<geometry_msgs::Twist> sub("robot_cmdVel", &messageCb ); //Se suscribe al topic robot_cmdVel para recibir las velocidades

void setup()
{ 
  Motor1.run(RELEASE); 
  Motor2.run(RELEASE); 
  nh.initNode();
  nh.advertise(Position);
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
