import rospy
from geometry_msgs.msg import Twist, Vector3

def callback(data):
    rospy.loginfo("Motor speed: %s",data.data)
    
def listener():
    rospy.init_node('motor')
    rospy.Subscriber("motor_speed", Twist, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()