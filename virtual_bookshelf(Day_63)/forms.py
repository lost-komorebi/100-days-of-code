#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange, Length


class BookForm(FlaskForm):

    title = StringField(
        label="Book Name", validators=[
            InputRequired(
                message="Book Name cannot be empty"), Length(
                max=100, message="Maximum length is 100")], render_kw={
                    'style': 'width: 200px; margin:auto;'})
    author = StringField(
        label="Book Author", validators=[
            InputRequired(
                message="Book Author cannot be empty"), Length(
                max=50, message="Maximum length is 100")], render_kw={
                    'style': 'width: 200px; margin:auto;'})
    rating = IntegerField(
        label="Rating", validators=[
            InputRequired(
                message="Rating cannot be empty"), NumberRange(
                min=1, max=100, message="Rating must between 1 to 10")], render_kw={
                    'style': 'width: 200px; margin:auto;'})
    sub_btn = SubmitField(label="Add Book")
