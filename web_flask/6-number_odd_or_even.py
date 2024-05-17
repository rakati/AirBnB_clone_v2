#!/usr/bin/python3
'''A simple module with flask app'''
from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_route(n):
    '''router for route url'''
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    '''router for route url'''
    data = {
        'n': n
    }
    return render_template('5-number.html', data=data)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_template_route(n):
    '''router for route url'''
    data = {
        'n': n,
        'type': 'odd' if n % 2 == 1 else 'even'
    }
    return render_template('6-number_odd_or_even.html', data=data)


if __name__ == '__main__':
    app.run(port=5000)
