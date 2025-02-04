import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class Joy_sub(Node):
    def __init__(self):
        super().__init__('joy_sub')
        self.subscription = self.create_subscription(
            Joy,
            'joy_cmd',
            self.listener_callback,
            10
        )
        self.subscription 
       
    def listener_callback(self,msg):   
        self.get_logger().info(str(msg.axes))
        self.get_logger().info(str(msg.buttons))

def main(args=None):
    rclpy.init(args=args)
    joy_sub = Joy_sub()
    rclpy.spin(joy_sub)
    joy_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
