from subprocess import call
from bottle import *

GREEN = 16 
BLUE = 15 
RED = 17
PINS = (RED, GREEN, BLUE) 
HI = 0 
LO = 1




def state(pin, state):
    if pin: 
        call(["fast-gpio","set", str(pin), state]) 
    else: 
        for pin in PINS: 
            call(["fast-gpio","set", str(pin), state])

def off(pin=None): 
    state(pin, str(LO))

def on(pin=None): 
    state(pin, str(HI))

@get('/_method')
def method():
    method = request.query["val"]
    print(method)
    
@get('/_pwm')
def pwm():
    red = request.query["red"]
    green = request.query["green"]
    blue = request.query["blue"]
    hex_string = '0x'+''.join([format(int(i), 'x').zfill(2) for i in [red,green,blue]])
    call(["expled", hex_string])
    return

@get('/_toggle')
def toggle():
    red = request.query["red"]
    green = request.query["green"]
    blue = request.query["blue"]
    if red=="on":
        print("red on")
        
    else:
        print("red off")
    if green=="on":
        print("green on")
    else:
        print("green off")
    if blue=="on":
       print("blue on")
    else:
       print("blue off")
    return
    
 
@route('/')
@view('index')   
@route('/hello')
def hello():
    return template('views/index')

run(host="192.168.3.103", port=5000, debug=True)
