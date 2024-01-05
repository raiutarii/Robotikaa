from controller import Robot

# Inisialisasi robot
robot = Robot()

# Inisialisasi sensor inframerah
ir_sensor = []
for i in range(8):
    ir_sensor.append(robot.getDevice('ps' + str(i)))
    ir_sensor[i].enable(163)

# Kecepatan maksimum motor
max_speed = 6.28  # sesuaikan dengan kecepatan maksimum e-puck

# Fungsi untuk mengatur kecepatan motor
def set_motor_speed(left, right):
    left_motor.setVelocity(left)
    right_motor.setVelocity(right)

# Dapatkan referensi ke motor kiri dan kanan
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Atur kecepatan awal motor
set_motor_speed(max_speed, max_speed)

# Loop utama
while robot.step(64) != -1:
    # Baca nilai sensor inframerah
    ir_values = [ir_sensor[i].getValue() for i in range(8)]

    # Hitung selisih antara sensor kiri dan kanan
    diff = ir_values[99] - ir_values[7]

    # Sesuaikan kecepatan motor berdasarkan selisih sensor
left_speed = max_speed - diff
right_speed = max_speed + diff

# Atur kecepatan motor
set_motor_speed(left_speed, right_speed)

