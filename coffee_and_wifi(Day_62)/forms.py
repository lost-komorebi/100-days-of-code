#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, URL


class CafeForm(FlaskForm):
    cafe_name = StringField(
        label="Cafe Name",
        validators=[
            InputRequired(
                message="Cafe Name cannot be empty")],
        render_kw={
            "has-error": False})
    loc = StringField(
        label="Cafe location on Google Maps(URL)", validators=[
            InputRequired(
                message="Location cannot be empty"), URL(
                message="Invalid URL")])
    open = StringField(label="Opening Time e.g. 8AM", validators=[
        InputRequired(
            message="Opening Time cannot be empty")])
    close = StringField(label="Closing Time e.g. 6PM", validators=[
        InputRequired(
            message="Closing Time cannot be empty")])
    coffee_rating = SelectField(label="Coffee Rating",
                                choices=[
                                    "☕" *
                                    i for i in range(
                                        1,
                                        6)])
    wifi_rating = SelectField(
        label="Wifi Strength Rating",
        choices=["✘"] + ["💪" * i for i in range(1, 6)])
    power_rating = SelectField(
        label="Power socket Availability",
        choices=["✘"] + ["🔌" * i for i in range(1, 6)])
    sub_btn = SubmitField(label="Submit")
