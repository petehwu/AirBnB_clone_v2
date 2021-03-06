#!/usr/bin/python3
""" This script starts a flask server and serves states list
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def show_states():
    """This method displays all the states in storage
    """
    s_list = list(storage.all("State").values())
    return render_template('7-states_list.html', s_list=s_list)


@app.teardown_appcontext
def close_storage(exception):
    """this method closes the storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
