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


@app.route('/states', strict_slashes=False)
def states():
    all_states = storage.all("State")
    return render_template('9-states.html', states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    all_states = storage.all("State")
    if id:
        try:
            all_states = all_states['State.{}'.format(id)]
        except KeyError:
            id = None
    return render_template('9-states.html', states=all_states, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
