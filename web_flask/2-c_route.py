#!/usr/bin/python3

""" A script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Message displayed when function is called """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Message displayed when function is called """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Message displayed when function is called """
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    """ Calling main function """

    app.run(host='0.0.0.0', port=5000)
