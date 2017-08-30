import RPi.GPIO as gpio
from sense_hat import SenseHat
import time
import json
from flask import Flask, redirect, render_template, url_for, request
from drivers import go_forward, backward, left, right, pivot_right, stop

app = Flask(__name__)
#gpio.setmode(gpio.BOARD)
#sense = SenseHat()


@app.route("/")
@app.route("/<int:key>")
def home(key=None):
    stop()    
    if key == 1:
        stop()
        go_forward()
        print("you hit key 1")
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
    fwd = request.get_data(as_text=True)
    print(fwd)

    if fwd == 'forward':
        print("moving moving", fwd)
        go_forward()
  
    return None


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
