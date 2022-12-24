#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional


class LoginForm(FlaskForm):
    email = StringField(
        '', validators=[
            DataRequired(), Length(
                max=50), Email()], render_kw={
            'placeholder': 'Email'})
    password = PasswordField('', validators=[DataRequired()], render_kw={
        'placeholder': 'Password'})
    sub_btn = SubmitField('Log me in!')


class RegisterForm(FlaskForm):
    username = StringField(
        '', validators=[
            DataRequired(), Length(
                max=50)], render_kw={
            'placeholder': 'Name'})
    email = StringField(
        '', validators=[
            DataRequired(), Length(
                max=50), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField(
        '', validators=[
            DataRequired()], render_kw={
            'placeholder': 'Password'})
    sub_btn = SubmitField('Sign me up!')


class AddToDoListForm(FlaskForm):
    detail = StringField(
        '', validators=[
            DataRequired()], render_kw={
            'placeholder': 'Add New...'})
    due_date = DateField(
        '', validators=[Optional()])
    btn = SubmitField('ADD')
