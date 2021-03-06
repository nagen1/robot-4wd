import RPi.GPIO as gpio
from sense_hat import SenseHat
import time
import json
from flask import Flask, redirect, render_template, url_for, request
from drivers import go_forward, backward, left, right, pivot_right, stop, servo

app = Flask(__name__)
#gpio.setmode(gpio.BOARD)
#sense = SenseHat()


@app.route("/")
@app.route("/<int:key>")
def home(key=None):
    servo(0)
    stop()
    if key == 1:
        stop()
        go_forward()
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
    if key == 7:
        stop()
        servo(120)

    return render_template('/home.html')

# Webhook works with IFTTT and google assistant response message. 
# once IFTTT funtion gets POST message from google assistant, it acts on the given task.
@app.route('/ifttt', methods=['GET', 'POST'])
def ifttt():
    fwd = request.get_data(as_text=True)
    print(fwd)
    new = fwd.split()
    print(new[1])

    if new[1] == 'forward':
        go_forward()
    elif new[1] == 'back' or new[1] == 'backward':
        backward()
    elif new[1] == 'right':
        right()
    elif new[1] == 'left':
        left()
    elif new[1] == 'stop':
        stop()
    elif new[1] == 'circle' or new[1] == 'round' or new[1] == 'clock':
        pivot_right()
    elif new[1] == 'clean':
        servo(120)
        go_forward()
    elif new[1] == 'rest':
        stop()
        servo(0)
  
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

        return redirect(url_for('home'), code=302)

@app.route('/test')
def test():
    try:
        with open('data.json') as json_data:
            data = json.load(json_data)
    except:
        data = {}
    keys = data.keys()
    newstring = data['Sensor']
    
    return redirect(url_for('home'))
                    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)

