#include <Servo.h>
#include <ros.h>
#include <geometry_msgs/Twist.h>

Servo Servo1; //Hombro            
Servo Servo2; //Base
Servo Servo3; //Garra 

int Hombro; 
int Base; 
int Garra;        

ros::NodeHandle  nh;
geometry_msgs::Twist tw_msg;

void messageCb( const geometry_msgs::Twist& robot_pinza){
  Hombro = robot_pinza.linear.y;
  Base = robot_pinza.linear.x;
  Garra = robot_pinza.linear.z;
  
 //Abrir garra
  if(Garra>0){
  Servo3.write(180);  
  }
  
  //Cerrar garra
  if(Garra<0){
  Servo3.write(0);
  }

  //BASE
  if (Base>0) { //if Value read of the button ==LOW:
    Servo2.write(Base); //servo goes to variable pos
    delay(10); //5 milliseconds of delay    
  }
  
  //HOMBRO
  if (Hombro>0) { //if Value read of the button ==LOW:
    Servo1.write(Hombro); //servo goes to variable pos
    delay(10); //5 milliseconds of delay    
  }
}

ros::Subscriber<geometry_msgs::Twist> sub("robot_garra", &messageCb ); //Se suscribe al topic robot_cmdVel para recibir las velocidades

void setup()
{   
  // Define the servo signal pins
  Servo1.attach (10); //Hombro      
  Servo2.attach (9); //Base
  Servo3.attach (3); //Garra rr
  // Posiciones iniciales
  Servo1.write(0);
  Servo2.write(70);
  Servo3.write(180);
  nh.initNode();
  nh.subscribe(sub); //CAR GAR
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
