#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///cafes.db'
    )

    Bootstrap(app)
    db.init_app(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from views import cafe_bp
    app.register_blueprint(cafe_bp)
    #app.add_url_rule('/', endpoint='index')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
