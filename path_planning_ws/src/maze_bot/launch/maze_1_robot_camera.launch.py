import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from scripts import GazeboRosPaths

def _launch_setup(context):
    package_share_dir = get_package_share_directory("maze_bot")
    urdf_file = os.path.join(package_share_dir, "urdf", "maze_bot.urdf")
    maze_id = LaunchConfiguration("maze_id").perform(context)
    if maze_id not in ["1", "2"]:
        maze_id = "2"
    world_file = os.path.join(package_share_dir, "worlds", "maze_{}.world".format(maze_id))

    model_path, plugin_path, media_path = GazeboRosPaths.get_paths()
    env = {
        "GAZEBO_MODEL_PATH": model_path, # as we only to add maze_bot(model) into gazebo models path
        "GAZEBO_PLUGIN_PATH": plugin_path,
        "GAZEBO_RESOURCE_PATH": media_path,
    }
    return [
        ExecuteProcess(
            cmd=["gazebo","--verbose",world_file,"-s","libgazebo_ros_factory.so",],
            output="screen",
            additional_env=env,
        ),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            arguments=[urdf_file],
        ),
    ]

def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "maze_id",
                default_value="2",
                description="Maze world to load: 1 or 2",
            ),
            OpaqueFunction(function=_launch_setup),
        ]
    )