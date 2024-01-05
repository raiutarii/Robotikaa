"""Daffa Asyqar Ahmad Khalisheka"""
"""1103200034"""
"""UTS Robotika Telkom University"""
"""2023"""


# Mengimpor modul 'Robot' dari pustaka 'controller' dalam Webots
from controller import Robot

# Fungsi untuk menjalankan logika robot mengikuti dinding
def run_robot(robot):
    """Wall following robot"""

    # Mendapatkan nilai timestep dari lingkungan simulasi
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28  # Kecepatan maksimum robot

    # Mengaktifkan motor kiri dan kanan
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    
    # Mengatur motor agar berputar tanpa batas dan memiliki kecepatan awal 0
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)

    # Mengaktifkan sensor jarak sebanyak 8 buah
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(timestep)
    
    # Loop utama:
    # - melakukan langkah simulasi hingga Webots menghentikan kontroler
    while robot.step(timestep) != -1:
        # Membaca nilai sensor jarak dan mencetaknya ke konsol
        for ind in range(8):
            print("ind: {}, val: {}".format(ind, prox_sensors[ind].getValue()))
    
        # Memproses data sensor
        left_wall = prox_sensors[5].getValue() > 80
        left_corner = prox_sensors[6].getValue() > 80
        front_wall = prox_sensors[7].getValue() > 80

        # Mengatur kecepatan motor kiri dan kanan berdasarkan logika kontrol
        left_speed = max_speed
        right_speed = max_speed

        if front_wall:
            print("Turn right in place")
            left_speed = max_speed
            right_speed = -max_speed
        else:
            if left_wall:
                print("Drive forward")
                left_speed = max_speed
                right_speed = max_speed
            else:
                print("Turn left")
                left_speed = max_speed / 8
                right_speed = max_speed

            if left_corner:
                print("Came too close, drive right")
                left_speed = max_speed
                right_speed = max_speed / 8

        # Mengatur kecepatan motor kiri dan kanan
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

# Kode untuk membersihkan setelah kontrol selesai (tidak diimplementasikan)
# Enter here exit cleanup code.

# Membuat instance dari robot dan menjalankan fungsi run_robot
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
