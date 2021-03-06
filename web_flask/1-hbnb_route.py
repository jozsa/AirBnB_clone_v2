#!/usr/bin/python3
"""
Defines rules for people accessing
various parts of my web app.
"""
from flask import Flask
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
