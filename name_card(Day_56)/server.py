#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
