import RPi.GPIO as gpio
import sys
import time
import curses

'''Config GPIO Ports'''
a = 7
b = 11
c = 13
d = 15

'''Initialize and setup GPIO ports open and ready'''
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(a, gpio.OUT)
    gpio.setup(b, gpio.OUT)
    gpio.setup(c, gpio.OUT)
    gpio.setup(d, gpio.OUT)

'''Move 4 wheels turn forward'''
def forward(tf):
    gpio.output(a, False)
    gpio.output(b, True)
    gpio.output(c, True)
    gpio.output(d, False)
    time.sleep(tf)
    gpio.cleanup()


'''Move 4 wheels turn backward'''
def reverse(tf):
    gpio.output(a, True)
    gpio.output(b, False)
    gpio.output(c, False)
    gpio.output(d, True)
    time.sleep(tf)
    gpio.cleanup()


'''left turn'''
def left_turn(tf):
    gpio.output(a, True)
    gpio.output(b, True)
    gpio.output(c, True)
    gpio.output(d, False)
    time.sleep(tf)
    gpio.cleanup()


'''Right turn'''
def right_turn(tf):
    gpio.output(a, False)
    gpio.output(b, True)
    gpio.output(c, False)
    gpio.output(d, False)
    time.sleep(tf)
    gpio.cleanup()


'''Pivot left turn'''
def pivot_left(tf):
    gpio.output(a, True)
    gpio.output(b, False)
    gpio.output(c, True)
    gpio.output(d, False)
    time.sleep(tf)
    gpio.cleanup()


'''Pivot right turn'''
def pivot_right(tf):
    gpio.output(a, False)
    gpio.output(b, True)
    gpio.output(c, False)
    gpio.output(d, True)
    time.sleep(tf)
    gpio.cleanup()
    

def rover():
    #clear screen	
    key_press = ''
    while 1:
        init()
        key_press = sys.stdin.read(1)
        sleep_time = 0.030
        if key_press == 'w':
            forward(sleep_time)
        elif key_press == 's':
            reverse(sleep_time)
        elif key_press == 'a':
            left_turn(sleep_time)
        elif key_press == 'd':
            right_turn(sleep_time)
        elif key_press == 'f':
            pivot_right(sleep_time)
        elif key_press == 'l':
            pivot_left(sleep_time)
        else:
            gpio.cleanup()
            break
    
curses.initscr()
curses.noecho()
curses.cbreak()
rover()
#sleep_time = 0.3
