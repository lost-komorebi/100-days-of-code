#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from app import db


class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean)
    has_toilet = db.Column(db.Boolean)
    has_wifi = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)
