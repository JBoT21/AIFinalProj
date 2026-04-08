import sys
import os
import time

# Point Python to the real SDK location
sys.path.append('/home/pi/TurboPi/')

from HiwonderSDK.mecanum_control import chassis   
import HiwonderSDK.Sonar as Sonar                 
import HiwonderSDK.Board as Board                

# ── Sonar setup ────────────────────────────────────────────
sonar = Sonar.Sonar()

def get_distance():
    """Returns distance in cm from the ultrasonic sensor."""
    dist = sonar.getDistance()
    return dist if dist > 0 else 999  # 999 = no reading / open space

# ── Motion helpers ─────────────────────────────────────────
# direction: 90=forward, 270=back, 0=right, 180=left
# yaw: -2.0 to 2.0 (negative=counter-clockwise, positive=clockwise)

def move_forward(speed=60):
    chassis.set_velocity(speed, 90, 0)

def move_backward(speed=40):
    chassis.set_velocity(speed, 270, 0)

def turn_left(speed=50, yaw=-0.6):
    chassis.set_velocity(speed, 90, yaw)

def turn_right(speed=50, yaw=0.6):
    chassis.set_velocity(speed, 90, yaw)

def strafe_left(speed=50):
    chassis.set_velocity(speed, 180, 0)

def strafe_right(speed=50):
    chassis.set_velocity(speed, 0, 0)

def stop():
    chassis.set_velocity(0, 90, 0)

def move(speed, turn):
    if speed == 0:
        stop()
    else:
        direction = 90 if speed > 0 else 270
        chassis.set_velocity(abs(speed), direction, turn)
