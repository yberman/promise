from bottle import route, run, abort, static_file
from time import sleep
from random import random

@route('/sleep/<time:int>')
def api(time):
    sleep(time)
    if random() < 0.2:
        # Fail
        return abort(500, "random server failure")
    return {"status": "success"}

@route('/')
def index():
    return static_file('index.html', root='.')

run(host='localhost', port=8080)
