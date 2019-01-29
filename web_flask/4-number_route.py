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
def show_c(text):
    """This method prints out some text
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def show_py(text='is cool'):
    """This method prints out some text
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def show_num(n):
    """This method prints out some text
    """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
