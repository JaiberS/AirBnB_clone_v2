#!/usr/bin/python3
""" Flask """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ string to be returned """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ string to be returned """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ string to be returned """
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    """ string to be returned """
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ string to be returned """
    return '{} is a number'.format(n).replace('_', ' ')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
