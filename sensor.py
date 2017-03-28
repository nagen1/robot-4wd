import RPi.GPIO as gpio
import time

trig = 38
echo = 40

gpio.setmode(gpio.BOARD)
gpio.setup(trig, gpio.OUT)
gpio.output(trig, 0)

gpio.setup(echo, gpio.IN)

time.sleep(0.1)

print("starting measuring")

gpio.output(trig, 1)
time.sleep(0.00001)
gpio.output(trig, 0)

while gpio.input(echo) == 0:
    pass
start = time.time()

while gpio.input(echo) ==1:
    pass
stop = time.time()

result = (stop - start) * 17000
print(result)

gpio.cleanup() 
