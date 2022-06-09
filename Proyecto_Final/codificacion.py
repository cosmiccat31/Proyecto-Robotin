#!/usr/bin/env python3
from matplotlib.pyplot import imshow
import rospy
from sensor_msgs.msg import Image

# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import pytesseract
#from cv2 import *
# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
bridge = CvBridge()

def captura(Imagen):
    # cam_port = 2
    # cam = VideoCapture(cam_port)
    # reading the input using the camera
    #result, image = Imagen.read()
    image = Imagen
    # If image will detected without any error,
    # show result
    # if result:

    #     grayImage = cvtColor(image, COLOR_BGR2GRAY)
    #     #imshow("GeeksForGeeks", grayImage)
    #     #imwrite("GeeksForGeeks.png", image)
    #     #waitKey(0)
    #     #destroyWindow("GeeksForGeeks")

    # else:
    #     print("No image detected. Please! try again")
    #grayImage = cvtColor(image, COLOR_BGR2GRAY)
    #Lectura de texto
    return(pytesseract.image_to_string(image))

def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError:
        print(CvBridgeError,'error')
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)
    imagenLeida = cv2.imread('camera_image.jpeg')
    grayImage = cv2.cvtColor(imagenLeida, cv2.COLOR_BGR2GRAY)   
    print(pytesseract.image_to_string(grayImage)) 
    

def main():
    rospy.init_node('image_listener')
    rate = rospy.Rate(10)
    # Define your image topic
    image_topic = "/usb_cam/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    
    # Spin until ctrl + c
    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    main()