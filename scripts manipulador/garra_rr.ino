#include <Servo.h>
#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Vector3.h>
//------Declaración de los Servos-----
Servo Servo1; //Hombro            
Servo Servo2; //Base
Servo Servo3; //Garra 

//-----Declaración de variables-------
//Variables que reciben las velocidades 
int Hombro; 
int Base; 
int Garra;        
//Variables de posicion
int posH=90;
int posB=80;
int posG=180;

ros::NodeHandle  nh;
geometry_msgs::Twist tw_msg;//Recibe
geometry_msgs::Vector3 v3_msg;//Envia

//********************PUBLISHER*********************
ros::Publisher Angle("robot_angulo", &v3_msg);

//*****************FUNCION CALLBACK*********************
void messageCb( const geometry_msgs::Twist& robot_pinza){
  
  Hombro = robot_pinza.linear.x;
  Base = robot_pinza.linear.y;
  Garra = robot_pinza.linear.z;
  
 //Abrir
  if(Garra>0){
     if (posG<180){
    posG=posG+5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    }
    else{
    posG=180;
    }
  Servo3.write(180);  
  }
  //Cerrar
  if(Garra<0){
      if (posG>0){
    posG=posG-5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    }
    else{
    posG=0;
    }
  Servo3.write(0);
  }

  //Izquierda
  if (Base>0) { 
     if (posB<180){
   posB=posB+5;   //increases the value of the "pos" variable each time the push button of the left is pressed
    }
    else{
    posB=180;
    }
    delay(5); //5 milliseconds of delay
    Servo2.write(posB); //servo goes to variable pos
    
  }
  //Derecha
  if(Base<0) { //if Value read of the button ==LOW:
    if (posB>0){
   posB=posB-5;   //increases the value of the "pos" variable each time the push button of the left is pressed
    }
    else{
    posB=0;
    }
    delay(5); //5 milliseconds of delay
    Servo2.write(posB); //servo goes to variable pos
  }

  //Arriba
  if (Hombro>0) { //if Value read of the button ==LOW:
    if (posH<180){
    posH=posH+5;  //increases the value of the "pos" variable each time the push button of the left is pressed
    }
    else{
    posH=180;
    }
    delay(5); //5 milliseconds of delay
    Servo1.write(posH); //servo goes to variable pos
    
  }
  //Abajo
  if(Hombro<0) { //if Value read of the button ==LOW:
    if (posH>0){
   posH=posH-5;   //increases the value of the "pos" variable each time the push button of the left is pressed
    }
    else{
    posH=0;
    }
    delay(5); //5 milliseconds of delay
    Servo1.write(posH); //servo goes to variable pos
  }
}

ros::Subscriber<geometry_msgs::Twist> sub("robot_pinza", &messageCb ); //Se suscribe al topic robot_cmdVel para recibir las velocidades
//322 442 0404 // FOOD, SABROSO
void setup()
{   
  // Define the servo signal pins
  Servo1.attach (10); //Hombro      
  Servo2.attach (9); //Base
  Servo3.attach (3); //Garra rr
  // Posiciones iniciales
  Servo1.write(0);
  Servo2.write(80);
  Servo3.write(0);
  nh.initNode();
  nh.advertise(Angle);
  nh.subscribe(sub);
}

void loop()
{  
  v3_msg.x = Servo1.read(); //Hombro
  v3_msg.y = Servo2.read(); //Base
  v3_msg.z = 15;
  Angle.publish(&v3_msg);
  nh.spinOnce();
  delay(1);
}
