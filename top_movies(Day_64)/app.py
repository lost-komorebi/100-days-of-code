#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# bootstrap
Bootstrap(app)
# session
app.config["SESSION_TYPE"] = 'filesystem'
app_session = Session(app)
# sqlite
db_file = 'movies.db'
absolute_path = os.path.abspath(db_file)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + absolute_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
