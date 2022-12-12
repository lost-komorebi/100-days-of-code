#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import InputRequired


class ImgForm(FlaskForm):

    img = FileField(
        label='Upload Image',
        validators=[
            InputRequired(
                message='Please upload picture!')],
        render_kw={
            'class': 'btn_upload', 'onchange': 'form.submit()'})
