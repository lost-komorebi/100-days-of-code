#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def greet():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt>'


@app.route('/<int:number>')
def guess_number(number):
    n = randint(0, 9)
    if number < n:
        return '<h1 style="color:red">Too low,try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt>'
    elif number > n:
        return '<h1 style="color:blue">Too high,try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt>'
    else:
        return '<h1 style="color:pink">You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt>'


if __name__ == '__main__':
    app.run(debug=True)
