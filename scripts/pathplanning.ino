//-------------------------LIBRERIAS----------------------------------//
#include "TimerOne.h"
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;    //Manejador del nodo

//-----------------------------------------------------------------------//
//                     CONSTANTES Y VARIABLES                            //
//-----------------------------------------------------------------------//

// Constante para pasos del disco
const float stepcount = 20.00;  // 20 Slots in disk, change if different
 
// Constante para el diametro de la rueda
const float wheeldiameter = 68; // Wheel diameter in millimeters, change if different
 
// Contadores
volatile int counter_A = 0;
volatile int counter_B = 0;

//Constantes del motor
const int enA = 6;
const int in1 = 7;
const int in2 = 8;
const int in3 = 9;
const int in4 = 10;
const int enB = 11;

const int speed = 130;      //Velocidad en PWM

// Constants for Interrupt Pins
// Change values if not using Arduino Uno
 
const byte MOTOR_A = 3;  // Motor 2 Interrupt Pin - INT 1 - Right Motor
const byte MOTOR_B = 2;  // Motor 1 Interrupt Pin - INT 0 - Left Motor
 
// Float for number of slots in encoder disk
float diskslots = 20;  // Change to match value of encoder disk
String info;

// Recibir ordenes de posición
void messageCb( const std_msgs::String& orden){
  info = orden.data;
}

// Topic direcciones: recibe las ordenes que robotin debe seguir para llegar a una posición deseada
ros::Subscriber<std_msgs::String> sub("/direcciones", messageCb ); 

// Interrupt Service Routines
 
// Motor A pulse count ISR
void ISR_countA()  
{
  counter_A++;  // increment Motor A counter value
} 
 
// Motor B pulse count ISR
void ISR_countB()  
{
  counter_B++;  // increment Motor B counter value
}
 

// Function to convert from centimeters to steps
int CMtoSteps(float cm) {
 
  int result;  // Final calculation result
  float circumference = (wheeldiameter * 3.14) / 10; // Calculate wheel circumference in cm
  float cm_step = circumference / stepcount;  // CM per Step
  
  float f_result = cm / cm_step;  // Calculate result as a float
  result = (int) f_result; // Convert to an integer (note this is NOT rounded)
  return result;  // End and return result
}

// Function to Move Forward
void MoveForward(int steps, int mspeed) 
{
   counter_A = 0;  //  reset counter A to zero
   counter_B = 0;  //  reset counter B to zero
   
   // Set Motor A forward
   digitalWrite(in1, HIGH);
   digitalWrite(in2, LOW);
 
   // Set Motor B forward
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);

   analogWrite(enA, mspeed);
   analogWrite(enB, mspeed);
   // Go forward until step value is reached
   while (true) {
   //Serial.println(counter_A);
    if (steps <counter_A) {
    analogWrite(enA, 0);
    } 

    if (steps < counter_B) {
    analogWrite(enB, 0);
  } 
  if (steps < counter_B && (steps < counter_A)){
  break;
   }
   }
}

// Function to Move in Reverse
void MoveReverse(int steps, int mspeed) 
{
   counter_A = 0;  //  reset counter A to zero
   counter_B = 0;  //  reset counter B to zero
   
   // Set Motor A reverse
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
 
  // Set Motor B reverse
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
   
   // Go in reverse until step value is reached
   while (steps > counter_A && steps > counter_B) {
   
    if (steps > counter_A) {
    analogWrite(enA, mspeed);
    } else {
    analogWrite(enA, 0);
    }
    if (steps > counter_B) {
    analogWrite(enB, mspeed);
    } else {
    analogWrite(enB, 0);
    }
    }
    
  // Stop when done
  analogWrite(enA, 0);
  analogWrite(enB, 0);
  counter_A = 0;  //  reset counter A to zero
  counter_B = 0;  //  reset counter B to zero 
 
}
 
// Function to Spin Right
void SpinRight(int steps, int mspeed) 
{
   counter_A = 0;  //  reset counter A to zero
   counter_B = 0;  //  reset counter B to zero
   
   // Set Motor A reverse
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
 
  // Set Motor B forward
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
   
   // Go until step value is reached
   while (steps > counter_A && steps > counter_B) {
   
    if (steps > counter_A) {
    analogWrite(enA, mspeed);
    } else {
    analogWrite(enA, 0);
    }
    if (steps > counter_B) {
    analogWrite(enB, mspeed);
    } else {
    analogWrite(enB, 0);
    }
   }
    
  // Stop when done
  analogWrite(enA, 0);
  analogWrite(enB, 0);
  counter_A = 0;  //  reset counter A to zero
  counter_B = 0;  //  reset counter B to zero 
 
}
 
// Function to Spin Left
void SpinLeft(int steps, int mspeed) 
{
   counter_A = 0;  //  reset counter A to zero
   counter_B = 0;  //  reset counter B to zero
   
   // Set Motor A forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
 
  // Set Motor B reverse
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
   
   // Go until step value is reached
   while (steps > counter_A && steps > counter_B) {
   
    if (steps > counter_A) {
    analogWrite(enA, mspeed);
    } else {
    analogWrite(enA, 0);
    }
    if (steps > counter_B) {
    analogWrite(enB, mspeed);
    } else {
    analogWrite(enB, 0);
    }
  }
    
  // Stop when done
  analogWrite(enA, 0);
  analogWrite(enB, 0);
  counter_A = 0;  //  reset counter A to zero
  counter_B = 0;  //  reset counter B to zero 
 
}
 
void setup() 
{
  Serial.begin(9600);
  
  // Attach the Interrupts to their ISR's
  attachInterrupt(digitalPinToInterrupt (MOTOR_A), ISR_countA, RISING);  // Increase counter A when speed sensor pin goes High
  attachInterrupt(digitalPinToInterrupt (MOTOR_B), ISR_countB, RISING);  // Increase counter B when speed sensor pin goes High

  
 //   SpinLeft(CMtoSteps(26), 180);  // Forward half a metre at 255 speed
 //   delay(1000);
 //   MoveForward(CMtoSteps(80), 180);  // Forward half a metre at 255 speed
  //  delay(1000);
 //   SpinRight(CMtoSteps(26), 180);  // Forward half a metre at 255 speed
 //   delay(1000);
 //   MoveReverse(CMtoSteps(80), 180);  // Forward half a metre at 255 speed
  //Serial.print(counter_A);
  // Test Motor Movement  - Experiment with your own sequences here  
  nh.initNode();
  nh.subscribe(sub);
} 
 
void loop()
{
  if(info =="adelante"){
      MoveForward(CMtoSteps(10), 150);  // Forward half a metre at 255 speed
    }

  if(info =="izquierda"){
      SpinLeft(CMtoSteps(10), 150);  // Forward half a metre at 255 speed
    }

  if(info =="derecha"){
      SpinRight(CMtoSteps(10), 150);  // Forward half a metre at 255 speed
    }  

  Serial.print(info);
  //Cosa ros
  nh.spinOnce(); 
  delay(1);  
}
