import RPi.GPIO as gpio
import time
from tkinter import *

gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT)
pwm = gpio.PWM(40, 100)

pwm.start(5)

def servo(angle):
    #scale = Scale(angle)
    duty = float(angle)/10.0+2.5
    print(duty)
    pwm.ChangeDutyCycle(duty)

servo(0)
time.sleep(1)
servo(120)
time.sleep(2)

gpio.cleanup()
