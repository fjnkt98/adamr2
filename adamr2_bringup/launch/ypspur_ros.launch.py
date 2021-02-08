import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros


def generate_launch_description():
    descriptions = launch.LaunchDescription()

    config_filepath = launch.substitutions.LaunchConfiguration(
            'config_filepath')
    param_filepath = launch.substitutions.LaunchConfiguration('param_filepath')
    device_path = launch.substitutions.LaunchConfiguration('device_path')

    declare_config_filepath = launch.actions.DeclareLaunchArgument(
            'config_filepath',
            default_value=os.path.join(
                get_package_share_directory('adamr2_bringup'),
                'config',
                'ypspur_ros.config.yaml'
                )
            )

    declare_param_filepath = launch.actions.DeclareLaunchArgument(
            'param_filepath',
            default_value=os.path.join(
                get_package_share_directory('adamr2_bringup'),
                'config',
                'adamr2.param'
                )
            )

    declare_device_path = launch.actions.DeclareLaunchArgument(
            'device_path',
            default_value='/dev/ttyACM0'
            )

    ypspur_coordinator = launch.actions.ExecuteProcess(
            cmd=[
                'ypspur-coordinator',
                '-p',
                param_filepath,
                '-d',
                device_path,
                '--without-device',
                '--without-control'
                ],
            output='screen'
            )
    ypspur_ros_node = launch_ros.actions.Node(
            package='ypspur_ros2',
            executable='ypspur_ros2_node',
            name='ypspur_ros2_node',
            parameters=[config_filepath],
            output='screen'
            )

    descriptions.add_action(declare_config_filepath)
    descriptions.add_action(declare_param_filepath)
    descriptions.add_action(declare_device_path)
    descriptions.add_action(ypspur_coordinator)
    descriptions.add_action(ypspur_ros_node)

    return descriptions
