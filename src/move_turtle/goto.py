#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def goto():
    # Initialize the ROS node
    rospy.init_node('goto', anonymous=True)

    # Create a publisher for the goal position
    goal_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)

    # Define the list of points to visit
    points = [
        (1.0, 1.0, 0.0),
        (2.0, 2.0, 0.0),
        (3.0, 3.0, 0.0)
    ]

    # Define the number of cycles to perform
    num_cycles = 3

    # Loop through the cycles
    for _ in range(num_cycles):
        # Loop through the points and send them as goals
        for point in points:
            goal = PoseStamped()
            goal.header.frame_id = 'map'
            goal.pose.position.x = point[0]
            goal.pose.position.y = point[1]
            goal.pose.position.z = point[2]
            goal_pub.publish(goal)
            rospy.sleep(5)  # Delay to allow time for the robot to reach the goal


if __name__ == '__main__':
    try:
        goto()
    except rospy.ROSInterruptException:
        pass
