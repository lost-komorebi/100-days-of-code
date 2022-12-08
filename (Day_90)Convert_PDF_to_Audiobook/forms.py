#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class PdfForm(FlaskForm):
    pdf = FileField(
        label='Please upload *.pdf file.',
        validators=[
            FileRequired(
                message='File is required!')],
        render_kw={'class': 'form-control', 'style': 'width:20%'})
    btn = SubmitField('Convert')
