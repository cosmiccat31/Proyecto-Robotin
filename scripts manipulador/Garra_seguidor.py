#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
import serial
from geometry_msgs.msg import Twist


def talker():
    global tw
    pub = rospy.Publisher('/robot_pinza', Twist, queue_size=10)
    rospy.init_node('turtle_bot_teleop', anonymous=True)
    rate = rospy.Rate(10)  # posible cambio

    tw = Twist()

    COM = '/dev/cu.usbserial-14120'
    BAUD = 9600
    # ser = serial.Serial(COM, BAUD)

    cap = cv2.VideoCapture(0)
    azulBajo = np.array([90, 100, 20], np.uint8)
    azulAlto = np.array([120, 255, 255], np.uint8)

    while not rospy.is_shutdown():

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

                        if x < 80:
                            if y < 60:
                                print("Cuadrante 1,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                               

                            elif 120 > y >= 60:
                                print("Cuadrante 1,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 1,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 1,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 1,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 1,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                
                            elif 360 <= y < 420:
                                print("Cuadrante 1,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 1,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif 160 > x >= 80:

                            if y < 60:
                                print("Cuadrante 2,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 2,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 2,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 2,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 2,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 2,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 360 <= y < 420:
                                print("Cuadrante 2,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 2,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif 240 > x >= 160:

                            if y < 60:
                                print("Cuadrante 3,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 3,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 3,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 3,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 3,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 3,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 360 <= y < 420:
                                print("Cuadrante 3,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 3,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif 240 <= x < 320:

                            if y < 60:
                                print("Cuadrante 4,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 4,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 4,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 4,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 4,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 4,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 360 <= y < 420:
                                print("Cuadrante 4,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 4,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif 320 <= x < 400:

                            if y < 60:
                                print("Cuadrante 5,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 5,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 5,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 5,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 5,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 5,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 360 <= y < 420:
                                print("Cuadrante 5,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 5,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif 400 <= x < 480:

                            if y < 60:
                                print("Cuadrante 6,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 6,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 6,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 6,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 6,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 6,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                
                            elif 360 <= y < 420:
                                print("Cuadrante 6,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 6,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif 480 <= x < 560:

                            if y < 60:
                                print("Cuadrante 7,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 7,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 7,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 7,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 7,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 7,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                
                            elif 360 <= y < 420:
                                print("Cuadrante 7,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 7,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                        elif x >= 560:

                            if y < 60:
                                print("Cuadrante 8,1")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                print(frame.shape)

                            elif 120 > y >= 60:
                                print("Cuadrante 8,2")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 > y >= 120:
                                print("Cuadrante 8,3")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 180 <= y < 240:
                                print("Cuadrante 8,4")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 240 <= y < 300:
                                print("Cuadrante 8,5")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)

                            elif 300 <= y < 360:
                                print("Cuadrante 8,6")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)
                                
                            elif 360 <= y < 420:
                                print("Cuadrante 8,7")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                                

                            elif y >= 420:
                                print("Cuadrante 8,8")
                                tw.linear.y=float(-180)
                                tw.linear.x = float(-60)                       
                            
                            pub.publish(tw)
                            rate.sleep()
        # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                    #ser.close()
                 break
    cap.release()
    cv2.destroyAllWindows()
                            


if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass
