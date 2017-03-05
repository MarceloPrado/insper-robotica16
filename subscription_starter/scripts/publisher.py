import rospy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import String


def scaneou(dado):
	print(min(dado.ranges))

	


if __name__=="__main__":

	output_speed = rospy.Publisher("/motor_speed", Twist, queue_size = 3 )
	rospy.init_node("motor")

	while not rospy.is_shutdown():
		speed = Twist(Vector3(10, 0, 0), Vector3(0, 0, 0))
		output_speed.publish(speed}{})
		rospy.sleep(2)
