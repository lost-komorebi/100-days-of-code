#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask
from views import image_bp
from flask_bootstrap import Bootstrap


def create_app():

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    app.register_blueprint(image_bp)
    Bootstrap(app)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True, port=5001)
