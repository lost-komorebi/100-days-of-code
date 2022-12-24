#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


from datetime import date, datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    to_do_lists = relationship('ToDoList', back_populates='user')
    # set default value from server
    create_time = db.Column(db.DateTime, server_default=func.now())


class ToDoList(db.Model):
    __tablename__ = 'to_do_lists'
    id = db.Column(db.INTEGER, primary_key=True)
    detail = db.Column(db.String(250), nullable=False)
    status = db.Column(db.INTEGER, default=-1)
    is_delete = db.Column(db.INTEGER, default=0)
    user = relationship('User', back_populates='to_do_lists')
    user_id = db.Column(db.INTEGER, db.ForeignKey('users.id'), nullable=False)
    due_date = db.Column(db.Date)
    # set default value from server
    create_time = db.Column(db.DateTime, server_default=func.now())
