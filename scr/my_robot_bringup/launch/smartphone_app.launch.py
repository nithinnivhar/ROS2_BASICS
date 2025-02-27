from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_names=["Giskard","BB8","Daneel","Jander","C3PO"]

    robot_news_station_node=[]

    for name in robot_names:
        robot_news_station_node.append(Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_"+name.lower(),
        parameters=[{"robot_name":name}]

        ))

    smartphone_node=Node(
        package="my_py_pkg",
        executable="smartphone",
        name="smartphone"

    )

    for node in robot_news_station_node:
        ld.add_action(node)
    ld.add_action(smartphone_node)
    return ld