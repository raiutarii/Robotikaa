from controller import Robot, Camera, Motor
import math

# Function to calculate the angle between the robot and the goal
def calculate_angle(x_robot, z_robot, x_goal, z_goal):
    angle = math.atan2(z_goal - z_robot, x_goal - x_robot)
    return angle

# Function to control the ePuck to face the goal
def face_goal(robot, camera):
    # Get camera image
    image = camera.getImage()
    
    # Get image width and height
    width = camera.getWidth()
    height = camera.getHeight()
    
    # Calculate the center of the image
    center_x = width / 2
    center_z = height / 2
    
    # Get the position of the goal in the image
    x_goal, z_goal = camera.getBallPosition(image)
    
    if x_goal != -1 and z_goal != -1:
        # Get the position of the robot
        x_robot, _, z_robot = robot.getFromCamera(0, center_x, center_z)
        
        # Calculate the angle between the robot and the goal
        angle = calculate_angle(x_robot, z_robot, x_goal, z_goal)
        
        # Set the wheel speeds to rotate the robot towards the goal
        left_speed = 1.0 - angle
        right_speed = 1.0 + angle
        
        # Set motor speeds
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    else:
        # If the goal is not in the camera view, stop the robot
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)

# Create the robot instance
robot = Robot()

# Get the time step of the current world
timestep = int(robot.getBasicTimeStep())

# Enable the camera
camera = robot.getCamera("camera")
camera.enable(timestep)

# Enable the motors
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Main control loop
while robot.step(timestep) != -1:
    # Call the function to face the goal
    face_goal(robot, camera)
