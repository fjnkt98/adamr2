import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions

def generate_launch_description():
    device_port = launch.substitutions.LaunchConfiguration('device_port')
    config_path = launch.substitutions.LaunchConfiguration('config_path')

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('device_port', default_value='/dev/input/js0'),
        launch.actions.DeclareLaunchArgument('config_path', default_value=[launch.substitutions.TextSubstitution(text=os.path.join(get_package_share_directory('adamr2_bringup'), 'config', 'joy.config.yml'))]),

        launch_ros.actions.Node(
            package='joy',
            node_executable='joy_node',
            name='joy_node',
            parameters=[{
                'dev': device_port,
                'deadzone': 0.3,
                'autorepeat_rate': 20.0
            }]
        ),
        launch_ros.actions.Node(
            package='teleop_twist_joy',
            node_executable='teleop_node',
            name='teleop_twist_joy_node',
            parameters=[config_path]
        )
    ])