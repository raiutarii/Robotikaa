from controller import Robot, Motor

# Create the Robot instance
robot = Robot()

# Get handles to the motors and set target position to infinity
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set up the time, speed, and other parameters
time_step = 70  # Lower time step for more precise control
speed = 1.0  # Adjust speed as needed
turn_time = 2.1  # Time to turn (in seconds)

# Main control loop
while robot.step(time_step) != -1:
    # Stop the robot
    left_motor.setVelocity(0.5)
    right_motor.setVelocity(0.5)
    robot.step(int(turn_time * 800))  # Stop for turn_time milliseconds
    
    # Turn right
    left_motor.setVelocity(speed)
    right_motor.setVelocity(-speed)
    robot.step(int(turn_time * 500))  # Turn right for half of turn_time milliseconds
    
    # Move forward
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)
    robot.step(int(turn_time * 5000))  # Move straight for turn_time milliseconds
    
    # Stop the robot
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    robot.step(int(turn_time * 1000))  # Stop for turn_time milliseconds
    
    # Turn right again
    left_motor.setVelocity(speed)
    right_motor.setVelocity(-speed)
    robot.step(int(turn_time * 500))  # Turn right for half of turn_time milliseconds

    # Move forward once more
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)
    robot.step(int(turn_time * 1000))  # Move straight for turn_time milliseconds
    
    # Stop the robot (you can remove this if you want continuous movement)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
