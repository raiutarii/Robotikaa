from controller import Robot, Motor

# Inisialisasi robot
robot = Robot()

# Inisialisasi motor
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set kecepatan maksimum
max_speed = 6.28
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(max_speed)
right_motor.setVelocity(max_speed)

# Loop utama
while robot.step(64) != -1:
    # Mendapatkan waktu simulasi
    current_time = robot.getTime()

    # Contoh 1: Robot tidak dapat menyelesaikan tugas dalam waktu singkat
    if current_time < 2.0:
        # Tidak ada tindakan khusus yang diambil, biarkan robot bergerak dengan kecepatan maksimum
        pass  # Placeholder to indicate no action

    # Contoh 2: Robot dapat berputar 360 derajat dalam 4 detik
    elif 2.0 <= current_time < 6.0:
        # Setel kecepatan untuk berputar 360 derajat dalam 4 detik
        left_motor.setVelocity(max_speed / 2)
        right_motor.setVelocity(-max_speed / 2)

    # Hentikan robot setelah mencapai waktu tertentu
    elif current_time >= 10.0:
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
        break

# Cleanup
robot.cleanup()
