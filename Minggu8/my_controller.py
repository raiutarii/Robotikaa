from controller import Robot, Motor

# Create the Robot instance
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Get the motors and set position sensors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set the maximum motor speed in rad/s
max_speed = 6.28

# Initialize variables
start_time = robot.getTime()
distance_traveled = 0.0

# Main loop
while robot.step(timestep) != -1:
    current_time = robot.getTime()

    # Example 1: Robot cannot exceed 6.28 rad/s
    if current_time < 2.0:
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(max_speed)
    else:
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)

    # Example 2: Robot moves 10 inches south in 10 seconds
    if current_time < 15.0:
        left_motor.setPosition(10.0 / (2 * 3.14 * 0.035))  # 0.035 is the wheel radius
        right_motor.setPosition(10.0 / (2 * 3.14 * 0.035))
        distance_traveled = 10.0
    else:
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)

    # Example 3: Robot moves 10 inches north in 5 seconds
    if current_time < 10.0:
        left_motor.setPosition(-10.0 / (2 * 3.14 * 0.035))
        right_motor.setPosition(-10.0 / (2 * 3.14 * 0.035))
        distance_traveled = -10.0
    else:
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)

    # Print time and distance information
    print("Time: {:.2f} s, Distance: {:.2f} inches".format(current_time - start_time, distance_traveled))


