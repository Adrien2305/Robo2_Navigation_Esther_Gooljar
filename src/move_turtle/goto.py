#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def goto():
    # Initialize the ROS node
    rospy.init_node('move_turtle', anonymous=True)

    # Create a publisher for the goal position
    goal_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)

    # Define the list of points to visit
    points = [(3.0278525352478027, -1.4700452089309692), (7.72671127319336, -2.4896795749664307), (3.081020355224609, -2.7720134258270264)]

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
