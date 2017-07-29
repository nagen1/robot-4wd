import RPi.GPIO as gpio
from sense_hat import SenseHat
import time
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
#gpio.setmode(gpio.BOARD)
sense = SenseHat()

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)  #input 3
    gpio.setup(8, gpio.OUT)   #input 1
    gpio.setup(10, gpio.OUT)  #input 2
    gpio.setup(12, gpio.OUT)  #input 4   

def text():
    text_color = (255, 0, 0)
    background = (255, 255, 255)
    speed = 0.25
    message = "Hi"
    sense.show_message(message, speed, text_colour = text_color, back_colour = background)
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

@app.route("/")
@app.route("/<int:key>")
def home(key=None):
    stop()    
    if key == 1:
        forward()
    if key == 2:
        stop()
        left()
    if key == 3:
        stop()
        backward()
    if key == 4:
        stop()
        right()
    if key == 5:
        stop()
    if key == 6:
       stop()
       pivot_right()

    return render_template('/home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
