import sys
import os
import time

# Point Python to the real SDK location
sys.path.append('/home/raspberrypi/TurboPi/TurboPi/')

import HiwonderSDK.mecanum as mecanum
import HiwonderSDK.Sonar as Sonar

# ── Sonar setup ────────────────────────────────────────────
sonar = Sonar.Sonar()

def get_distance():
    """Returns distance in cm from the ultrasonic sensor."""
    dist = sonar.getDistance()
    return dist if dist > 0 else 999  # 999 = no reading / open space

# ── Motion helpers ─────────────────────────────────────────
def move_forward(speed=60):
    mecanum.setVelocity(speed, 90, 0)

def move_backward(speed=40):
    mecanum.set_velocity(speed, 270, 0)

def turn_left(speed=50, yaw=-0.6):
    mecanum.set_velocity(speed, 90, yaw)

def turn_right(speed=50, yaw=0.6):
    mecanum.set_velocity(speed, 90, yaw)

def strafe_left(speed=50):
    mecanum.set_velocity(speed, 180, 0)

def strafe_right(speed=50):
    mecanum.set_velocity(speed, 0, 0)

def stop():
    mecanum.set_velocity(0, 90, 0)

def move(speed, turn):
    """
    Main movement function used by navigation.
    speed: -100 to 100 (negative = backward)
    turn: -2.0 to 2.0 (negative = left, positive = right)
    """
    if speed == 0:
        stop()
    else:
        direction = 90 if speed > 0 else 270
        mecanum.set_velocity(abs(speed), direction, turn)