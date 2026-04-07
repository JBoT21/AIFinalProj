# The base driver for moving, stopping, and scanning
import RPi.GPIO as GPIO
from hiwonder.TurboPiCar import TurboPiCar
import hiwonder.Sonar as Sonar
import cv2, numpy as np

car = TurboPiCar()
sonar = Sonar.Sonar()

def get_distance():
    return sonar.getDistance()  # cm

def move(speed, turn):
    #speed: -100 to 100, turn: -1.0 to 1.0
    car.set_velocity(speed, 90 + int(turn * 30), 0)

def stop():
    car.set_velocity(0, 90, 0)
