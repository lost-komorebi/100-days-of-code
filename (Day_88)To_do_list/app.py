#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        SQLALCHEMY_DATABASE_URI='sqlite:///to_do_list.db',
        # SQLALCHEMY_ECHO=True  # print sql
    )

    Bootstrap(app)

    from models import db, User, ToDoList
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    from auth import login_manager
    login_manager.init_app(app)

    @app.route('/')
    def index():
        return render_template('auth/index.html')

    from auth import auth_bp
    app.register_blueprint(auth_bp)

    from to_do_list import to_do_list_bp
    app.register_blueprint(to_do_list_bp)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
