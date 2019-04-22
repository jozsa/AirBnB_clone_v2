#!/usr/bin/python3
"""
Defines return values for people requesting
various parts of my web app
"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB to anyone who submits
    a GET request to my app"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Returns "HBNB" to anyone who submits a
    GET request to my web server at /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C' followed by the value of
    the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Returns 'Python' followed by the value
    of the text variable. If nothing is passed,
    'Python is cool' is returned"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    """Returns <n> is a number only if a number is typed
    into the URL"""
    try:
        int(n)
        return '{} is a number'.format(n)
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template_n(n):
    """Displays a HTML page only if n is an integer"""
    try:
        int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
