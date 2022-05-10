#include <SoftwareSerial.h>
#include <Servo.h>

//Declaramos el servo
Servo servo;
Servo servoG;

//Declaramos la variable
char dato;
int angulo = 90;
int anguloG = 180;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  servo.attach(9);
  servo.write(angulo);
  servoG.attach(3);
  servoG.write(anguloG);
}

void loop() {
  while(Serial.available()){
    dato = Serial.read();
    delay(10);
    Serial.println(dato);
    switch(dato){
      case 'd':
      //Gira servo hacia la derecha
      angulo = angulo + 1;
      servo.write(angulo);
      break;
      
      case 'l':
      //Gira servo hacia la izquierda
      angulo = angulo - 1;
      servo.write(angulo);
      break;
      
      case 'p':
      //Parar el servo
      angulo = angulo;
      servo.write(angulo);
      break;

      case 'i':
      //Parar el servo
      anguloG = 0;
      servoG.write(anguloG);
      break;

      case 'u':
      //Parar el servo
      anguloG = 180;
      servoG.write(anguloG);
      break;
      }
   }
 }
