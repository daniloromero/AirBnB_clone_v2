#!/usr/bin/python3
"""script that starts Flask web applicationlistening on 0.0.0.0 port 5000"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all States"""
    states_list = storqage.all(State).values()

    return render_template('7-states_list.html', states=states_list)

if __name__ == "__main__":
    """ Main Function"""
    app.run(host='0.0.0.0', port=5000)
