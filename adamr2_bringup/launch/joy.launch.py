import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros


def generate_launch_description():
    descriptions = launch.LaunchDescription()

    device_path = launch.substitutions.LaunchConfiguration('device_path')
    config_path = launch.substitutions.LaunchConfiguration('config_path')

    declare_device_path = launch.actions.DeclareLaunchArgument(
            'device_path',
            default_value='/dev/input/js0'
            )

    declare_config_path = launch.actions.DeclareLaunchArgument(
            'config_path',
            default_value=os.path.join(
                get_package_share_directory('adamr2_bringup'),
                'config',
                'joy.config.yaml'
                )
            )

    joy_node = launch_ros.actions.Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{
                'dev': device_path,
                'deadzone': 0.3,
                'autorepeat_rate': 20.0
                }]
            )

    teleop_twist_joy_node = launch_ros.actions.Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy_node',
            parameters=[config_path]
            )

    descriptions.add_action(declare_config_path)
    descriptions.add_action(declare_device_path)
    descriptions.add_action(joy_node)
    descriptions.add_action(teleop_twist_joy_node)

    return descriptions
