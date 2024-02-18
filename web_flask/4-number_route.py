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
def cisfun(text):
    """ Message displayed when function is called.
        Display c followed by the value of the text variable.
    """
    return "C " + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """ Display Python , followed by the
        value of the text variable (replace underscore _ symbols with a space )
        The default value of text is is cool.
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display number: display `n` is a number only if n is an integer """
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    """ Calling main function """

    app.run(host='0.0.0.0', port=5000)
