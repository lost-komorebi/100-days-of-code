#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField
from wtforms.validators import Length, URL, DataRequired


class CafeForm(FlaskForm):
    name = StringField(label='NAME', validators=[DataRequired(), Length(max=250)])
    map_url = StringField(label='MAP_URL', validators=[DataRequired(), URL(), Length(max=500)])
    img_url = StringField(label='IMG_URL', validators=[DataRequired(), URL(), Length(max=500)])
    location = StringField(label='LOCATION', validators=[DataRequired(), Length(max=250)])
    has_sockets = BooleanField(label='HAS_SOCKETS')
    has_toilet = BooleanField(label='HAS_TOILET')
    has_wifi = BooleanField(label='HAS_WIFI')
    can_take_calls = BooleanField(label='CAN_TAKE_CALLS')
    seats = IntegerField(label='SEATS NUMBER', validators=[DataRequired()])
    coffee_price = FloatField(
        label='COFFEE_PRICE(£)',
        validators=[
            DataRequired()])
    btn = SubmitField(label='ADD', render_kw={'type': 'button', 'class': 'btn btn-primary'})
