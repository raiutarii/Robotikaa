from controller import Robot

# Initialize the robot
robot = Robot()

# Get the devices
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set initial robot pose
robot_pose = {'x': 0, 'y': 0, 'grid_number': 1, 'orientation': 'N'}

# Main loop
while robot.step(64) != -1:
    # Move the robot forward
    left_motor.setVelocity(2.0)
    right_motor.setVelocity(2.0)

    # Update robot pose based on movement (this is a simplistic example)
    robot_pose['x'] += 1
    robot_pose['y'] += 1

    # Check if the robot is in a visited cell and update the grid
    if robot_pose['grid_number'] == 3 and robot_pose['x'] == 2 and robot_pose['y'] == 2:
        print("Cell visited!")
        # Update the grid (assuming a 4x4 grid)
        print("|x . . .|\n|. . . .|\n|x x x x|\n|. . . x|")

    # Print the current robot pose
    print("Robot Pose:", robot_pose)

# End the program
