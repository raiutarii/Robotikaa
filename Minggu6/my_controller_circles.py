from controller import Robot, Motor, Supervisor
import time

# Set up the robot
robot = Robot()
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")

# Get the time step of the simulation
time_step = int(robot.getBasicTimeStep())

# Function to convert degrees to radians
def deg_to_rad(degrees):
    return degrees * 3.14159 / 180.0

# Set the speed of the motors
speed = 100  # adjust the speed as needed
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(speed)
right_motor.setVelocity(speed)

# Given parameters
radius1 = 0.1  # replace with your desired radius1
radius2 = 0.2  # replace with your desired radius2
time_per_loop = 10  # replace with your desired time for one loop

# Infinite loop for continuous figure-eight motion
while True:
    # Calculate the arc lengths for the given radii
    arc_length1 = 2 * 3.14159 * radius1
    arc_length2 = 2 * 3.14159 * radius2

    # Calculate the speeds for the left and right motors to achieve figure-eight
    left_speed = (arc_length1 / time_per_loop) * (180.0 / 3.14159)
    right_speed = (arc_length2 / time_per_loop) * (180.0 / 3.14159)

    # Set the velocities for the left and right motors for the first loop
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

    # Run the robot for the specified time for the first loop
    start_time = time.time()
    while robot.step(time_step) != -1:
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_per_loop:
            break

    # Stop the robot after the first loop
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

    # Print the degrees the robot has turned for the first loop
    degrees_turned = arc_length1 / radius1
    print("Degrees turned in the first loop:", degrees_turned)

    # Add a delay between each loop
    time.sleep(1)

    # Set the velocities for the left and right motors for the second loop (opposite direction)
    left_motor.setVelocity(-left_speed)
    right_motor.setVelocity(-right_speed)

    # Run the robot for the specified time for the second loop (opposite direction)
    start_time = time.time()
    while robot.step(time_step) != -1:
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_per_loop:
            break

    # Stop the robot after the second loop
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

    # Print the degrees the robot has turned for the second loop
    degrees_turned = arc_length1 / radius1
    print("Degrees turned in the second loop:", degrees_turned)

    # Add a delay between each loop
    time.sleep(1)
