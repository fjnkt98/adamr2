import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions

def generate_launch_description():
    config_filepath = launch.substitutions.LaunchConfiguration('config_filepath')
    param_filepath = launch.substitutions.LaunchConfiguration('param_filepath')

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('config_filepath',
                            default_value=os.path.join(
                                get_package_share_directory('adamr2_bringup'),
                                'config',
                                'ypspur_ros.config.yml')
                            ),
        launch.actions.DeclareLaunchArgument('param_filepath',
                            default_value=os.path.join(
                                get_package_share_directory('adamr2_bringup'),
                                'config',
                                'adamr2.param')
                            ),
        launch_ros.actions.Node(
            package='ypspur_ros',
            node_executable='ypspur_ros',
            name='ypspur_ros',
            parameters=[config_filepath, {"param_file": param_filepath}],
            output='screen'
        )
    ])