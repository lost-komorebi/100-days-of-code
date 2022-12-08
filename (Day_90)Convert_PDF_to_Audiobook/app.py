#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask
from flask_bootstrap import Bootstrap
from views import tts_bp


def create_app():

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    Bootstrap(app)

    app.register_blueprint(tts_bp)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
