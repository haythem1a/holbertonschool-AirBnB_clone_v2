#!/usr/bin/python3
"""Module that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Display HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def text_C(text):
    """Display “C” followed by the value of the text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_Python(text='is cool'):
    """Display “Python”, followed by the value of the text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
