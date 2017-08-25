import RPi.GPIO as gpio
from sense_hat import SenseHat
import time
import json
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)
#gpio.setmode(gpio.BOARD)
#sense = SenseHat()

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)  #input 3
    gpio.setup(8, gpio.OUT)   #input 1
    gpio.setup(10, gpio.OUT)  #input 2
    gpio.setup(12, gpio.OUT)  #input 4   

'''def text():
    text_color = (255, 0, 0)
    background = (255, 255, 255)
    speed = 0.25
    message = "Hi"
    sense.show_message(message, speed, text_colour = text_color, back_colour = background)
    sense.clear()

@app.route('/sense')
def sens():
    text()    '''
    
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

@app.route('/forward', methods=['GET', 'POST'])
def forward():
    fwd = request.get_data()

    if fwd == 'forward':
        print("moving moving", fwd)
  
    return redirect(url_for('home'), code=200)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    try:
        with open('data.json') as json_data:
            data = json.load(json_data)
    except:
        data = {}

    if request.method == 'GET':
        return render_template('/settings.html', results=data)

    elif request.method == 'POST':
        name = request.form['title']
        type = request.form['type']
        gpio1 = request.form['gpio1']
        gpio2 = request.form['gpio2']
        gpio3 = request.form['gpio3']
        gpio4 = request.form['gpio4']
        data[name] = []
        data[name].append({"title": name,
                             "type": type,
                             "gpio1": gpio1,
                             "gpio2": gpio2,
                             "gpio3": gpio3,
                             "gpio4": gpio4})

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
