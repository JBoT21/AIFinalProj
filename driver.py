import sys
import os
import time

sys.path.append('/home/raspberrypi/TurboPi/TurboPi/')

import HiwonderSDK.mecanum as mecanum_mod
import HiwonderSDK.Sonar as Sonar

# ── Initialize chassis ─────────────────────────────────────
# Try all known class names used in different TurboPi SDK versions
if hasattr(mecanum_mod, "MecanumChassis"):
    mecanum = mecanum_mod.MecanumChassis()
elif hasattr(mecanum_mod, "Mecanum"):
    mecanum = mecanum_mod.Mecanum()
else:
    raise RuntimeError("No Mecanum chassis class found in HiwonderSDK.mecanum")

# Detect correct movement function name (varies across SDK versions)
if hasattr(mecanum, "set_velocity"):
    set_vel = mecanum.set_velocity
elif hasattr(mecanum, "setVelocity"):
    set_vel = mecanum.setVelocity
elif hasattr(mecanum, "setSpeed"):
    set_vel = mecanum.setSpeed
elif hasattr(mecanum, "setCarRun"):
    set_vel = mecanum.setCarRun
else:
    raise RuntimeError("No velocity-setting function found in chassis object")

# ── Sonar setup ────────────────────────────────────────────
sonar = Sonar.Sonar()

def get_distance():
    dist = sonar.getDistance()
    return dist if dist > 0 else 999

# ── Motion helpers ─────────────────────────────────────────
def move_forward(speed=60):
    set_vel(speed, 90, 0)

def move_backward(speed=40):
    set_vel(speed, 270, 0)

def turn_left(speed=50, yaw=-0.6):
    set_vel(speed, 90, yaw)

def turn_right(speed=50, yaw=0.6):
    set_vel(speed, 90, yaw)

def strafe_left(speed=50):
    set_vel(speed, 180, 0)

def strafe_right(speed=50):
    set_vel(speed, 0, 0)

def stop():
    set_vel(0, 90, 0)

def move(speed, turn):
    if speed == 0:
        stop()
    else:
        direction = 90 if speed > 0 else 270
        set_vel(abs(speed), direction, turn)
