import RPi.GPIO as gpio
import time

centerTrigger = 10
centerEcho = 8

def distance(trigger, echo):
    gpio.setmode(gpio.BOARD)
    gpio.setup(trigger, gpio.OUT)
    gpio.output(trigger, 0)

    gpio.setup(echo, gpio.IN)
    time.sleep(0.1)

    print("starting measuring")

    gpio.output(trigger, 1)
    time.sleep(0.00001)
    gpio.output(trigger, 0)

    while gpio.input(echo) == 0:
        start = time.time()
        pass
 
    while gpio.input(echo) ==1:
        stop = time.time()
        pass

    result = (stop - start) * 17000
    print(result)
    gpio.cleanup() 

distance(centerTrigger, centerEcho)
