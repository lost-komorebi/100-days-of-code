#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from app import db

# CREATE TABLE "movies" (
# 	"id"	INTEGER,
# 	"title"	varchar(50) not null,
# 	"year" INTEGER not null,
# 	"description" varchar(250) not null,
# 	"rating" float,
# 	"ranking" INTEGER,
# 	"review" varchar(100),
# 	"img_url" varchar(500) not null,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# );
# CREATE UNIQUE INDEX "unique_title"
# ON "movies" ("title");



class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(100))
    img_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return self.title
