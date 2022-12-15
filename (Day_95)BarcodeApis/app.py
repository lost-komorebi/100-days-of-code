#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask
from views import barcode_bp


def create_app():

    app = Flask(__name__)
    app.config.from_mapping(
        {'SECRET_KEY': 'dev'})

    @app.route('/')
    def info():
        return 'welcome!'

    app.register_blueprint(barcode_bp)

    return app


if __name__ == '__main__':
    barcode = create_app()
    barcode.run(debug=True, port=5001)
