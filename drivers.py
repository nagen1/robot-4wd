import RPi.GPIO as gpio
from sense_hat import SenseHat
import time

# sense = SenseHat()
dc_motor_IN1 = 35
dc_motor_IN2 = 36
dc_motor_IN3 = 37
dc_motor_IN4 = 38

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dc_motor_IN1, gpio.OUT)
    gpio.setup(dc_motor_IN2, gpio.OUT)
    gpio.setup(dc_motor_IN3, gpio.OUT)
    gpio.setup(dc_motor_IN4, gpio.OUT)

def text():
    text_color = (255, 0, 0)
    background = (255, 255, 255)
    speed = 0.025
    message = "Hi"
    sense.show_message(message, speed, text_colour=text_color, back_colour=background)
    sense.clear()

def go_forward():
    init()
    gpio.output(dc_motor_IN1, True)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, False)
    gpio.output(dc_motor_IN4, True)

def backward():
    init()
    gpio.output(dc_motor_IN1, False)
    gpio.output(dc_motor_IN2, True)
    gpio.output(dc_motor_IN3, True)
    gpio.output(dc_motor_IN4, False)

def right():
    init()
    gpio.output(dc_motor_IN1, True)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, False)
    gpio.output(dc_motor_IN4, False)

def left():
    init()
    gpio.output(dc_motor_IN1, False)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, False)
    gpio.output(dc_motor_IN4, True)

def pivot_right():
    init()
    gpio.output(dc_motor_IN1, True)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, True)
    gpio.output(dc_motor_IN4, False)

def stop():
    gpio.cleanup()
    
def servo(angle):
    gpio.setmode(gpio.BOARD)
    gpio.setup(40, gpio.OUT)
    pwm = gpio.PWM(40, 100)
    pwm.start(5)
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    #gpio.cleanup()