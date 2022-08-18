#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired, URL, Length


# class MoviesForm(FlaskForm):
#
#     year = IntegerField(
#         label="Year", validators=[
#             InputRequired(
#                 message="Year cannot be empty")])
#     description = StringField(
#         label="Description", validators=[
#             InputRequired(
#                 message="Description cannot be empty"), Length(
#                 max=250, message="maximum length is 250")])
#     rating = FloatField(
#         label="Rating", validators=[
#             InputRequired(
#                 message="Rating cannot be empty")])
#     ranking = IntegerField(
#         label="Ranking", validators=[
#             InputRequired(
#                 message="Ranking cannot be empty")])
#     review = StringField(
#         label="Review", validators=[
#             InputRequired(
#                 message="Review cannot be empty"), Length(
#                 max=100, message="maximum length is 100")])
#     img_url = StringField(
#         label="Img_url", validators=[
#             InputRequired(
#                 message="Img_url cannot be empty"), URL(
#                 message="Invalid url")])
#     sub_btn = SubmitField(label="Add")


class AddMovieTitleForm(FlaskForm):
    title = StringField(
        label="Title", validators=[
            InputRequired(
                message="Title cannot be empty"), Length(
                max=50, message="maximum length is 50")])
    sub_btn = SubmitField(label="Add")


class UpdateMovieForm(FlaskForm):
    rating = FloatField(
        label="Rating", validators=[
            InputRequired(
                message="Rating cannot be empty")])
    review = StringField(
        label="Review", validators=[
            InputRequired(
                message="Review cannot be empty"), Length(
                max=100, message="maximum length is 100")])
    sub_btn = SubmitField(label="Add")
