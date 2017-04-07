import RPi.GPIO as gpio
import time

centerTrigger = 37
centerEcho = 38
rightTrigger = 35
rightEcho = 36
leftTrigger = 33
leftEcho = 40


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

'''Move 4 wheels turn forward'''
def back(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


'''Move 4 wheels turn backward'''
def forward(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


'''left turn'''
def left_turn(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


'''Right turn'''
def right_turn(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


'''Pivot left turn'''
def pivot_left(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


'''Pivot right turn'''
def pivot_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

'''Sensor '''

def distance(trigger, echo):
    gpio.setmode(gpio.BOARD)
    gpio.setup(trigger, gpio.OUT)
    gpio.output(trigger, 0)
    gpio.setup(echo, gpio.IN)
    time.sleep(0.1)

    gpio.output(trigger, 1)
    time.sleep(0.00001)
    gpio.output(trigger, 0)

    while gpio.input(echo) == 0:
        start = time.time()
        pass

    while gpio.input(echo) == 1:
        stop = time.time()
        pass

    result = (stop - start) * 17000
    gpio.cleanup()
    return(result)


'''Main - testing ->
   Rover autonomous driving using 3 sensor data
   this seems working, can be moved to ROS base to use sensor data into topics'''

center = 0
right = 0
left = 0

try:
    while True:
        right = distance(rightTrigger, rightEcho)
        center = distance(centerTrigger, centerEcho)
        left = distance(leftTrigger, leftEcho)
        print("Center:", center, " Light:", right, " Left:", left)

        if center >= 30:
            forward(0.3)
        elif right >=30:
            pivot_right(0.3)
        elif left >= 30:
            pivot_left(0.30)
        else:
            back(0.50)

except KeyboardInterrupt:
    gpio.cleanup()