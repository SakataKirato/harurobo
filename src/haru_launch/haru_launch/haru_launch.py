from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    config_file_arg = DeclareLaunchArgument(
        "config_file",
        default_value="/path/to/config.json",
        description="Path to the config file",
    )

    return LaunchDescription(
        [
            config_file_arg,
            # joy_node の起動
            Node(
                package="joy", executable="joy_node", name="joy_node", output="screen"
            ),
            # joy_translate_node の起動
            Node(
                package="joy_translate",  # joy_translate_node が含まれているパッケージ名
                executable="joy_translate_node",
                name="joy_translate_node",
                prefix="xterm -e",
                output="screen",
            ),
            Node(
                package="haru_odrive",
                executable="od",
                parameters=[{"config_file": LaunchConfiguration("config_file")}],
                prefix="xterm -e",
                output="screen",
            ),
        ]
    )
