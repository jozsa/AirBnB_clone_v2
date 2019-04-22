#!/usr/bin/python3
"""
One function: Returns "Hello HBNB!" to
anyone submitting a GET request to '/'
on my app
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns Hello HBNB to anyone who submits
    a GET request to my app"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
