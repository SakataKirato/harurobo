import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import String

# from geometry_msgs.msg import Twist
from sensor_msgs.msg import Float32


# from rogidrive_msg.msg import RogidriveMessage


class JoyTranslate(Node):
    def __init__(self):
        super().__init__("joy_translate_node")
        self.publisher = self.create_publisher(Float32, "/motor0_speed", 10)
        self.subscription = self.create_subscription(
            Joy, "joy_cmd", self.listener_callback, 10
        )

    def listener_callback(self, joy):
        msg = Float32()
        # msg.name = "haru"
        # msg.mode = 0
        # msg.pos = 0.0
        # msg.current = 0.0
        msg.data = (
            -math.sin(math.pi / 4) * joy.axes[0]
            + math.cos(math.pi / 4) * joy.axes[1]
            - joy.axes[5]
            + joy.axes[2]
        )
        # self.vel.linear.y = 5*Joy.axes[0]
        # self.vel.angular.z  = -2*(Joy.axes[2]-1) + 2*(Joy.axes[5]-1)
        self.publisher.publish(msg)
        self.get_logger().info(f"Velocity: Linear = {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    joy_translate = JoyTranslate()
    rclpy.spin(joy_translate)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
