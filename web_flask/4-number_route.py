#!/usr/bin/python3
"""script that starts Flask web applicationlistening on 0.0.0.0 port 5000"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """ Display “C ” followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_is(text='is_cool'):
    """display “Python ”, followed by the value of the text variable"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """display “n is a number” only if n is an integer"""
    if n is int:
        return "{} is a number".format(n)

if __name__ == "__main__":
    """ Main Function"""
    app.run(host='0.0.0.0', port=5000)
