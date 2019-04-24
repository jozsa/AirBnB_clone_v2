#!/usr/bin/python3
"""
Starts a flask web app and defines
rules for routes
"""
import json
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    Removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    all_states = storage.all("State")
    return render_template('8-cities_by_states.html', states=all_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
