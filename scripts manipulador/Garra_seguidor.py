#!/usr/bin/env python3
import rospy
import threading
import cv2
import numpy as np
from geometry_msgs.msg import Twist

COM = '/dev/cu.usbserial-14120'
BAUD = 9600

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#colores

azulBajo = np.array([90, 100, 20], np.uint8)
azulAlto = np.array([120, 255, 255], np.uint8)

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

                if x < 87:
                    if y < 87:
                        tw.linear.x = 120
                        tw.linear.y = 40

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                elif 174 > x >= 87:

                    if y < 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                elif 261 > x >= 174:

                    if y < 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                elif 261 <= x < 348:

                    if y < 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                elif 348 <= x < 435:

                    if y < 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                elif 435 <= x < 522:

                    if y < 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

                elif x >= 522:

                    if y < 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 174 > y >= 87:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 > y >= 174:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 261 <= y < 348:
                        tw.linear.x = 0
                        tw.linear.y = 0

                    elif 348 <= y < 435:
                        tw.linear.x = 0
                        tw.linear.y = 0
                    elif 435 <= y < 522:
                        tw.linear.x = 0
                        tw.linear.y = 0
                    elif y >= 522:
                        tw.linear.x = 0
                        tw.linear.y = 0

        pub.publish(tw)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
