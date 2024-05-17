#!/usr/bin/python3
'''A simple module with flask app'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''router for route url'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(port=5000)
