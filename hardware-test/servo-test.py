import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT)
pwm = gpio.PWM(40, 100)

pwm.start(5)
pwm.ChangeDutyCycle(7.5)

gpio.cleanup()
