#!/usr/bin/python3
'''A simple module with flask app'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''router for route url'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''router for route url'''
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun_route(text):
    '''router for route url'''
    import re
    return 'C ' + re.sub('_', ' ', text)


@app.route('/python', strict_slashes=False,
           defaults={'text': 'is cool'})
@app.route('/python/<string:text>', strict_slashes=False)
def python_is_cool_route(text):
    '''router for route url'''
    import re
    return 'Python ' + re.sub('_', ' ', text)


if __name__ == '__main__':
    app.run(port=5000)
