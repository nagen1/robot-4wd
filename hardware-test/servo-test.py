import RPi.GPIO as gpio
import time
from tkinter import *

gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT)
pwm = gpio.PWM(40, 100)

pwm.start(5)
#pwm.ChangeDutyCycle(20)

class App:
    def __init__(self, master):
         frame = Frame(master)
         frame.pack()
         scale = Scale(frame, from_=0, to=180, orient=HORIZONTAL, command=self.update)
         scale.grid(row=0)
    def update(self, angle):
         duty = float(angle) / 10.0 + 2.5
         print(duty)
         pwm.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()

#gpio.cleanup()
