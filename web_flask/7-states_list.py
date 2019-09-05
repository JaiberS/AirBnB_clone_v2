#!/usr/bin/python3
""" Flask """
from flask import Flask, render_template
from models import storage
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_template(n):
    """ string to be returned """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_odd_or_even(n):
    """ string to be returned """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def hello_state():
    """ string to be returned """
    statequieto = storage.all('State')
    namedic = {}
    for i in statequieto:
        j = i.to_dict()
        namedic.setdefault(j["name"], j["id"])
    return render_template('7-states_list.html', states=namedic)


@app.teardown_appcontext
def idk(self):
    """ string to be returned """
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
