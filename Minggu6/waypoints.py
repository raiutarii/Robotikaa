# Import necessary modules
from controller import Robot, Motor

# Create the Robot instance
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Get motors and set up position sensors
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Define robot parameters
wheel_radius = 19  # Replace with the actual wheel radius of your ePuck
max_speed = 6.28  # Replace with the maximum speed of your ePuck's motors

# Given values
major_radius = 30  # Replace with your desired major radius
minor_radius = 10  # Replace with your desired minor radius
time = 10.0  # Replace with your desired time
speed = 5  # Replace with your desired speed

# Calculate the angular velocity
angular_velocity = speed / major_radius

# Calculate the total angle to cover the oval path
total_angle = 110  # Assuming a complete oval

# Calculate the time it takes to cover the entire oval
time_to_complete_oval = total_angle / angular_velocity

# Calculate the left and right wheel speeds
left_speed = angular_velocity * (major_radius - 0.11 * minor_radius)
right_speed = angular_velocity * (major_radius + 0.11 * minor_radius)

# Set the initial speeds for the motors
left_motor.setVelocity(left_speed)
right_motor.setVelocity(right_speed)

# Main loop
while robot.step(timestep) < time_to_complete_oval:
    pass

# Stop the robot
left_motor.setVelocity(0)
right_motor.setVelocity(0)
