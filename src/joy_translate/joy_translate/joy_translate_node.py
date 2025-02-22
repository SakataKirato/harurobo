import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import numpy as np
from geometry_msgs.msg import Twist

# from /home/a/harurobo/src/rogilinkFlex-ros2/rogilink_flex_lib import Publisher, Subscriber
from ctypes import c_bool

import yaml


# from std_msgs.msg import Float32
# from rogidrive_msg.msg import RogidriveMessage


# def load_config(file_path="/home/a/harurobo/src/joy_translate/config.yaml"):
#     with open(file_path, "r", encoding="utf-8") as file:
#         return yaml.safe_load(from rogilink_flex_lib import Publisher, Subscriberfile)


class JoyTranslate(Node):
    def __init__(self):
        super().__init__("joy_translate_node")

        # config = load_config()

        # self.linear_speedfactor = config["parameters"]["linear_speedfactor"]
        # self.angular_speedfactor = config["parameters"]["angular_speedfactor"]

        self.declare_parameter("linear_speedfactor", 0.5)
        self.declare_parameter("angular_speedfactor", 0.5)

        self.linear_speedfactor = self.get_parameter("linear_speedfactor").value
        self.angular_speedfactor = self.get_parameter("angular_speedfactor").value

        self.publisher = self.create_publisher(Twist, "pid_cmd_vel", 10)
        self.subscription = self.create_subscription(
            Joy, "joy", self.listener_callback, 10
        )

        # rogilinkflex
        # self.publisher_servo = Publisher(self, "servo", (c_bool))
        # rogilinkflex

        # self.publisher1 = self.create_publisher(Twist, "/motor1_speed", 10)
        # self.publisher2 = self.create_publisher(Twist, "/motor2_speed", 10)
        # self.publisher3 = self.create_publisher(Twist, "/motor3_speed", 10)

    def listener_callback(self, joy):
        msg = Twist()
        msg.linear.x = -(self.linear_speedfactor * joy.axes[0])
        msg.linear.y = self.linear_speedfactor * joy.axes[1]
        msg.angular.z = (-joy.axes[2] + joy.axes[5]) * self.angular_speedfactor
        self.publisher.publish(msg)
        # rogilinkflex
        # servo_msg = c_bool()
        # servo_msg.value = joy.buttons[0]
        # self.publisher_servo.publish((servo_msg))
        # rogilinkflex
        self.get_logger().info(
            f"Velocity: {msg.linear.x}, {msg.linear.y}, {msg.angular.z}"
        )

        # translate_velocity = np.array(
        #     [
        #         [
        #             -self.linear_speedfactor,
        #             self.linear_speedfactor,
        #             self.angular_speedfactor,
        #         ],
        #         [
        #             -self.linear_speedfactor,
        #             -self.linear_speedfactor,
        #             self.angular_speedfactor,
        #         ][
        #             self.linear_speedfactor,
        #             -self.linear_speedfactor,
        #             self.angular_speedfactor,
        #         ],
        #         [
        #             self.linear_speedfactor,
        #             self.linear_speedfactor,
        #             self.angular_speedfactor,
        #         ],
        #     ],
        # )

        # controller_velocity = np.array(
        #     [-joy.axes[0], joy.axes[1], -joy.axes[2] + joy.axes[5]]
        # )
        # msg1 = Twist()
        # msg2 = Twist()
        # msg3 = Twist()

        # msg0.data = 0.0
        # msg1.data = 0.0
        # msg2.data = 0.0
        # msg3.data = 0.0

        # for i in range(4):
        #     for j in range(3):
        #         if i == 0:
        #             msg0.data += translate_velocity[i][j] * controller_velocity[j]
        #         if i == 1:
        #             msg1.data += translate_velocity[i][j] * controller_velocity[j]
        #         if i == 2:
        #             msg2.data += translate_velocity[i][j] * controller_velocity[j]
        #         if i == 3:
        #             msg3.data += translate_velocity[i][j] * controller_velocity[j]

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
        # self.publisher1.publish(msg1)
        # self.publisher2.publish(msg2)
        # self.publisher3.publish(msg3)


def main(args=None):
    rclpy.init(args=args)
    joy_translate = JoyTranslate()
    rclpy.spin(joy_translate)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
