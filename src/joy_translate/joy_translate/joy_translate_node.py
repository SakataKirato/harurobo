import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import numpy as np


# from geometry_msgs.msg import Twist
from std_msgs.msg import Float32


# from rogidrive_msg.msg import RogidriveMessage


class JoyTranslate(Node):
    def __init__(self):
        super().__init__("joy_translate_node")
        self.publisher0 = self.create_publisher(Float32, "/motor0_speed", 10)
        self.publisher1 = self.create_publisher(Float32, "/motor1_speed", 10)
        self.publisher2 = self.create_publisher(Float32, "/motor2_speed", 10)
        self.publisher3 = self.create_publisher(Float32, "/motor3_speed", 10)
        self.subscription = self.create_subscription(
            Joy, "joy", self.listener_callback, 10
        )

    def listener_callback(self, joy):
        R = 2
        translate_velocity = np.array(
            [
                [-np.sqrt(2), np.sqrt(2), R],
                [-np.sqrt(2), -np.sqrt(2), R],
                [np.sqrt(2), -np.sqrt(2), R],
                [np.sqrt(2), np.sqrt(2), R],
            ],
        )

        controller_velocity = np.array(
            [joy.axes[0], joy.axes[1], -joy.axes[5] + joy.axes[2]]
        )

        msg0 = Float32()
        msg1 = Float32()
        msg2 = Float32()
        msg3 = Float32()

        msg0.data = 0.0
        msg1.data = 0.0
        msg2.data = 0.0
        msg3.data = 0.0

        for i in range(4):
            for j in range(3):
                if i == 0:
                    msg0.data += translate_velocity[i][j] * controller_velocity[j]
                if i == 1:
                    msg1.data += translate_velocity[i][j] * controller_velocity[j]
                if i == 2:
                    msg2.data += translate_velocity[i][j] * controller_velocity[j]
                if i == 3:
                    msg3.data += translate_velocity[i][j] * controller_velocity[j]
        # msg.name = "haru"
        # msg.mode = 0
        # msg.pos = 0.0
        # msg.current = 0.0
        # msg.data = (
        #     -math.sin(math.pi / 4) * joy.axes[0]
        #     + math.cos(math.pi / 4) * joy.axes[1]
        #     - joy.axes[5]
        #     + joy.axes[2]
        # )
        # self.vel.linear.y = 5*Joy.axes[0]
        # self.vel.angular.z  = -2*(Joy.axes[2]-1) + 2*(Joy.axes[5]-1)
        self.publisher0.publish(msg0)
        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)
        self.publisher3.publish(msg3)
        self.get_logger().info(
            f"Velocity: Motor0 = {msg0.data}, Motor1 = {msg1.data}, Motor2 = {msg2.data}, Motor3 = {msg3.data}"
        )


def main(args=None):
    rclpy.init(args=args)
    joy_translate = JoyTranslate()
    rclpy.spin(joy_translate)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
