#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    r = requests.get('https://api.npoint.io/8bf1adf44a846b4c103b')
    posts = r.json()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id_>')
def post(id_):
    r = requests.get('https://api.npoint.io/8bf1adf44a846b4c103b')
    posts = r.json()
    for post_ in posts:
        if post_['id'] == id_:
            return render_template('post.html', post_=post_)


if __name__ == '__main__':
    app.run(debug=True)
