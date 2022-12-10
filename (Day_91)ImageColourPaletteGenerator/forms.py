#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired


class ImgForm(FlaskForm):

    img = FileField(label='Please upload picture.', validators=[
                    InputRequired(message='Please upload picture!')])
    btn = SubmitField('UPLOAD')
