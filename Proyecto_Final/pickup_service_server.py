#!/usr/bin/env python3

from __future__ import print_function

from chueco_pkg.srv import pickup_service, pickup_serviceResponse
from chueco_pkg.msg import pickup_service_answer
import rospy

def handle_pickup_service(req):
    print("Returning response")
    ans = pickup_service_answer()
    ans.state=1
    ans.pickup_zone=1
    ans.pickup_zone_x=10
    ans.pickup_zone_y =20
    print(ans)
    return pickup_serviceResponse(ans)

def pickup_service_server():
    rospy.init_node('pickup_service_server')
    s = rospy.Service('pickup_service', pickup_service, handle_pickup_service)
    print("Send info")
    rospy.spin()

if __name__ == "__main__":
    pickup_service_server()
