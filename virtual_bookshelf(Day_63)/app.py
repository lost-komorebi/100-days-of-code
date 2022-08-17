#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.secret_key = "NFLvdiTYljeRPmiGpABfab57GHXevIlr"
db_file = 'bookshelf.db'
absolute_path = os.path.abspath(db_file)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + absolute_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)
