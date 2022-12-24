#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Blueprint, redirect, url_for, render_template, flash
from forms import LoginForm, RegisterForm
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
login_manager = LoginManager()


@auth_bp.route('/register', methods=["POST", "GET"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        if get_user_by_username(username) or get_user_by_email(email):
            flash('Existed username or email. Please login in.')
            return redirect(url_for('auth.login'))
        else:
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.password = generate_password_hash(
                register_form.password.data)
            try:
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
            else:
                login_user(new_user)
                return redirect(url_for('index'))
    return render_template('auth/register.html', form=register_form)


@auth_bp.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = get_user_by_email(email)
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('to_do_list.get_all_to_do_lists'))
            else:
                flash('Invalid email or password!')
        else:
            flash('Invalid email or password!')
    return render_template('auth/login.html', form=login_form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
