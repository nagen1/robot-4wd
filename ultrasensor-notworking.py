import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    trigger = 38
    echo = 40
    gpio.setmode(gpio.BOARD)
    gpio.setup(trigger, gpio.OUT)
    gpio.setup(echo, gpio.IN)

    gpio.output(trigger, False)
    time.sleep(0.5)

    gpio.output(trigger, True)
    time.sleep(0.00001)

    sig = time.time()
    nosig = time.time()

    while gpio.input(echo) == 0:
        nosig = time.time()

    while gpio.input(echo) == 1:
        sig = time.time()

    t1 = sig - nosig

    if measure == 'cm':
        distance = t1 / 0.000058
    elif measure == 'in':
        distance = t1 / 0.000148
    else:
        print("improper choice")
        distance = None

    gpio.cleanup()
    return distance

dist = distance('cm')
print(dist)
