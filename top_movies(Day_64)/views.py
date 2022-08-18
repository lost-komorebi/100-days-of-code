#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from app import app, db, app_session
from flask import render_template, redirect, url_for, request, session
from models import Movies
from forms import AddMovieTitleForm, UpdateMovieForm

import requests


@app.route("/")
def home():
    """order by ranking desc"""
    all_movies = Movies.query.order_by(-Movies.ranking).all()
    return render_template("index.html", all_movies=all_movies)


def get_movie_info(title):
    parameters = {
        "api_key": "f063b6e4b11f94a6aec95a0d8bae054f",
        "query": title
    }
    r = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params=parameters)
    return r.json()['results']


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieTitleForm()
    if request.method == "POST":
        movies_list = get_movie_info(form.title.data)
        session["movies"] = movies_list  # set session
        return redirect(url_for('select'))
    return render_template('add.html', form=form)


@app.route('/select', methods=["GET", "POST"])
def select():
    return render_template('select.html')


@app.route('/save-to-data/<int:movie_id>')
def save_to_data(movie_id):
    parameters = {
        "api_key": "f063b6e4b11f94a6aec95a0d8bae054f"
    }
    url = 'https://api.themoviedb.org/3/movie/' + str(movie_id)
    r = requests.get(url, params=parameters)
    result = r.json()
    movie = Movies()
    movie.title = result["original_title"]
    movie.year = result["release_date"].split('-')[0]
    movie.img_url = "https://image.tmdb.org/t/p/w500" + result["poster_path"]
    movie.description = result["overview"]
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('update', id=movie.id))


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    movie = Movies.query.get_or_404(id)
    form = UpdateMovieForm(obj=movie)
    form.sub_btn.label.text = 'Update'  # change button text
    if request.method == "POST":
        movie.rating = form.rating.data
        movie.review = form.review.data
        # db.session.add(movie)
        db.session.commit()
        update_ranking()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)


def update_ranking():
    """update rankings of all movies"""
    movies = Movies.query.order_by(Movies.rating).all()
    for i in movies:
        i.ranking = len(movies)-movies.index(i)
        db.session.commit()


@app.route('/delete/<int:id>')
def delete(id):
    movie_to_del = Movies.query.get_or_404(id)
    db.session.delete(movie_to_del)
    db.session.commit()
    return redirect(url_for('home'))


