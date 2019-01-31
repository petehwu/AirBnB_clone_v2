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
    s_list = list(storage.all("State").values())
    return render_template('7-states_list.html', s_list=s_list)


@app.route('/cities_by_states')
def show_cities_states():
    """This method displays all the cities by states
    """
    s_list = list(storage.all("State").values())
    return render_template('8-cities_by_states.html', s_list=s_list)


@app.route('/states')
@app.route('/states/<sid>')
def show_state_or_city(sid=None):
    """This method displays states or city states
    """
    if (sid):
        key = "State." + sid
        if key in states:
            return render_template('9-states.html',
                                   s_list=storage.all("State").get(key))
        else:
            return render_template('9-states.html', s_list=None)
    else:
        s_list = list(storage.all("State").values())
        return render_template('7-states_list.html', s_list=s_list)


@app.route('/hbnb_filters')
def show_hbnb():
    """This method will pass the filters into the template
    """
    s_list = list(storage.all("State").values())
    a_list = list(storage.all("Amenity").values())
    return render_template('10-hbnb_filters.html',
                           s_list=s_list, a_list=a_list)


@app.teardown_appcontext
def close_storage(exception):
    """this method closes the storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
