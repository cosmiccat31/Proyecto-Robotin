#!/usr/bin/env python3
import cv2
import numpy as np
import serial
import keyboard

com = serial.Serial("COM11", 9600, write_timeout= 10)
d = 'd'
i = 'i'
p = 'p'
l = 'l'
u = 'u'
cap = cv2.VideoCapture(0)

a=input("Ingrese el color que desea rastrear (R=Red, Y=Yellow, B=Blue)")

if a=="R" or a=="r":
    azulBajo=np.array([0, 100, 20], np.uint8)
    azulAlto=np.array([10, 255, 255], np.uint8)

if a=="B" or a=="b":
    azulBajo = np.array([90, 100, 20], np.uint8)
    azulAlto = np.array([120, 255, 255], np.uint8)

if a=="Y" or a=="y":
    azulBajo = np.array([20, 100, 20], np.uint8)
    azulAlto = np.array([40, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mascara = cv2.inRange(frameHSV, azulBajo, azulAlto)
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contornos, -1, (255, 0, 0), 4)
        cv2.imshow('frame', frame)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 6000:
                M = cv2.moments(c)
                if M["m00"] == 0:
                    M["m00"] = 1
                x = int(M["m10"] / M["m00"])
                y = int(M['m01'] / M['m00'])
                cv2.circle(frame, (x, y), 7, (0, 0, 255), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno], 0, (255, 0, 0), 3)

                # Mostramos toda la informacion
                # print("Puntos: ", resultado.detections)

                # Extraemos el ancho y el alto del frame
                al, an, c = frame.shape

                # Extraemos el medio de la pantalla
                centro = int(an / 2)

                if x < centro - 50:
                    # Movemos hacia la izquierda
                    print("Izquierda")
                    com.write(l.encode('ascii'))
                elif x > centro + 50:
                    # Movemos hacia la derecha
                    print("Derecha")
                    com.write(d.encode('ascii'))
                elif x == centro:
                    # Paramos el servo
                    print("Parar")
                    com.write(p.encode('ascii'))

                elif keyboard.is_pressed("u"):
                    print("Cerrar")
                    com.write(u.encode('ascii'))
                elif keyboard.is_pressed("i"):
                    print("Abrir")
                    com.write(i.encode('ascii'))

    cv2.imshow("Camara", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break
cap.release()
cv2.destroyAllWindows()
