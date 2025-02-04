import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class JoyTranslate(Node): 
    def __init__(self):
        super().__init__('joy_translate_node') 
        self.publisher = self.create_publisher(Twist,'cmd_vel', 10)
        self.subscription = self.create_subscription(Joy,'joy_cmd', self.listener_callback, 10)
        self.vel = Twist()

    def listener_callback(self, Joy): 
        self.vel.linear.x  = 2*Joy.axes[1]
        self.vel.linear.y = 5*Joy.axes[0]
        self.vel.angular.z  = -2*(Joy.axes[2]-1) + 2*(Joy.axes[5]-1)
        self.publisher.publish(self.vel)
        self.get_logger().info("Velocity: Linear=%f" % (Joy.axes[1])) 

def main(args=None):
    rclpy.init(args=args)
    joy_translate = JoyTranslate()
    rclpy.spin(joy_translate)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

