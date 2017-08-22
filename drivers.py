import RPi.GPIO as gpio
from sense_hat import SenseHat
import time

app = Flask(__name__)

# sense = SenseHat()

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)  # input 3
    gpio.setup(8, gpio.OUT)  # input 1
    gpio.setup(10, gpio.OUT)  # input 2
    gpio.setup(12, gpio.OUT)  # input 4


def text():
    text_color = (255, 0, 0)
    background = (255, 255, 255)
    speed = 0.025
    message = "Hi"
    sense.show_message(message, speed, text_colour=text_color, back_colour=background)
    sense.clear()


def forward():
    init()
    gpio.output(8, True)
    gpio.output(10, False)
    gpio.output(11, True)
    gpio.output(12, False)


def backward():
    init()
    gpio.output(8, False)
    gpio.output(10, True)
    gpio.output(11, False)
    gpio.output(12, True)


def right():
    init()
    gpio.output(8, True)
    gpio.output(10, False)
    gpio.output(11, False)
    gpio.output(12, False)


def left():
    init()
    gpio.output(8, False)
    gpio.output(10, False)
    gpio.output(11, True)
    gpio.output(12, False)


def pivot_right():
    init()
    gpio.output(8, True)
    gpio.output(10, False)
    gpio.output(11, False)
    gpio.output(12, True)


def stop():
    gpio.cleanup()
