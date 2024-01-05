from controller import Robot

# Inisialisasi robot
robot = Robot()

# Dapatkan kontrol roda robot
left_wheel = robot.getDevice('left wheel motor')
right_wheel = robot.getDevice('right wheel motor')

# Set mode kontrol ke MODE_VELOCITY (kecepatan konstan)
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
left_wheel.setVelocity(0.0)
right_wheel.setVelocity(0.0)

# Kecepatan maksimum yang diperbolehkan (6.28 inci/detik)
max_velocity = 6.28

# Contoh nilai x (jarak yang diinginkan) dan V (kecepatan konstan)
x = 12.0  # Misalnya, bergerak 12 inci
V = 2.0  # Misalnya, kecepatan konstan 2 inci/detik

# Menghitung waktu yang diperlukan untuk mencapai jarak x dengan kecepatan V
time = x / V

# Atur kecepatan konstan pada roda
left_wheel.setVelocity(V)
right_wheel.setVelocity(V)

# Jalankan robot selama waktu yang diperlukan
robot.step(int(time * 1000))  # Konversi waktu ke milidetik

# Hentikan robot
left_wheel.setVelocity(0)
right_wheel.setVelocity(0)

# Keluar dari simulasi
robot.cleanup()
