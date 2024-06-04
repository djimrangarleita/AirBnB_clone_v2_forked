#!/usr/bin/python3
"""Hello world application in flask, and another endpoint"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return string as response to the request"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return string as response to the request"""
    return 'HBNB'


@app.route('/c/<compliment>', strict_slashes=False)
def complimente_c(compliment):
    """Return string as response to the request with param"""
    return f"C {compliment.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
