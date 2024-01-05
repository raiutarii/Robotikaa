from controller import Robot

# Inisialisasi robot
robot = Robot()

# Inisialisasi motor
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")

# Radius lingkaran yang diinginkan (misalnya, 5 inches)
R1 = 5

# Kecepatan yang diinginkan (misalnya, 2 inches per detik)
V = 2

# Menghitung kecepatan roda kiri dan kanan berdasarkan radius dan kecepatan linier
left_motor.setVelocity(V / R1)
right_motor.setVelocity(-V / R1)

# Main loop
while robot.step(64) != -1:
    pass
