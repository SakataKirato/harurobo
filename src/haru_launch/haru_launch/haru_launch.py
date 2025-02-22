from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    config_file_arg = DeclareLaunchArgument(
        "config_file",
        default_value="/path/to/config.json",
        description="Path to the config file",
    )

    linear_speedfactor_arg = DeclareLaunchArgument(
        "ls", default_value="0.5", description="Linear speed"
    )
    angular_speedfactor_arg = DeclareLaunchArgument(
        "as", default_value="0.5", description="Angular speed"
    )

    linear_speedfactor = ParameterValue(LaunchConfiguration("ls"), value_type=float)
    angular_speedfactor = ParameterValue(LaunchConfiguration("as"), value_type=float)

    return LaunchDescription(
        [
            config_file_arg,
            linear_speedfactor_arg,
            angular_speedfactor_arg,
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
                parameters=[
                    {
                        "linear_speedfactor": linear_speedfactor,
                        "angular_speedfactor": angular_speedfactor,
                    }
                ],
            ),
            Node(
                package="haru_odrive",
                executable="od",
                parameters=[{"config_file": LaunchConfiguration("config_file")}],
                prefix="xterm -e",
                output="screen",
            ),
            # Node(
            #     package="rogilink_flex",
            #     executable="rogilink_flex",
            #     name="rogilink_flex",
            #     parameters=[
            #         {"config_path": "/home/a/harurobo/src/haru_launch/config.json"}
            #     ],
            # ),
        ]
    )
