#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from chueco_pkg.srv import *
from chueco_pkg.msg import pickup_service_answer

def pickup_service_client(a, b):
    rospy.wait_for_service('pickup_service')#Nombre del servicio
    try:
        pickup_service = rospy.ServiceProxy('pickup_service', Pickup_Service)
        resp1 = pickup_service(a, b)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = str(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print((a, b))
    print("%s,%s = %s"%(a, b, pickup_service_client(a, b)))
