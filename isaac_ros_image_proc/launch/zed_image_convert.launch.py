import os
from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    # Initialize the LaunchDescription object
    ld = LaunchDescription()

    # Container for image format converter, rectify, and resize nodes
    processing_container = ComposableNodeContainer(
        name='processing_container',
        namespace='',  # Global namespace, adjust if needed
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='isaac_ros_image_proc',
                plugin='nvidia::isaac_ros::image_proc::ImageFormatConverterNode',
                name='image_format_node_left',
                parameters=[{'encoding_desired': 'bgr8'}],  # Set to BGR8
                remappings=[
                    ('image_raw', '/zed/zed_node/left_raw/image_raw_color'),
                    ('image', '/input_image')
                ]
            ), 
        ],
        output='screen',  # Outputs to screen for debugging
    )

    # Add the container to LaunchDescription
    ld.add_action(processing_container)

    return ld

