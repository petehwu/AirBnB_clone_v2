#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """This method prints out some text
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def h2():
    """This method prints out some text
    """
    return 'HBNB'


@app.route('/c/<text>')
def show_text(text):
    """This method prints out some text
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
