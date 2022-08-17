#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from app import db


# CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title
# varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating
# INTEGER NOT NULL);
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.title
