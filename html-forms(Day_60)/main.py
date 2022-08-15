#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template(
            'index.html',
            username=username,
            password=password)
    elif request.method == "GET":
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
