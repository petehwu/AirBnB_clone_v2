#!/usr/bin/python3
""" This script starts a flask server and serves states list
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def show_states():
    """This method displays all the states in storage
    """
    states = storage.all("State")
    s_list = []
    for s in states.values():
        s_list.append(s)
    return render_template('7-states_list.html', s_list=s_list)


@app.route('/cities_by_states')
def show_cities_states():
    """This method displays all the cities by states
    """
    states = storage.all("State")
    s_list = []
    for s in states.values():
        s_list.append(s)
    return render_template('8-cities_by_states.html', s_list=s_list)


@app.teardown_appcontext
def close_storage(exception):
    """this method closes the storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
