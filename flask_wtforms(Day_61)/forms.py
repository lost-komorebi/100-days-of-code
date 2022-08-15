#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class MyForm(FlaskForm):
    email = EmailField(
        'Email: ', validators=[InputRequired(),
                               Email(
            message="Invalid email address"), Length(
            4, message="Field must be at least 4 characters long")])
    password = PasswordField(
        'Password: ',
        validators=[InputRequired(),
                    Length(
            7,
            message="Field must be at least 8 characters long")])
    submit = SubmitField("Log In")
