#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from app import app, db
from forms import BookForm
from flask import render_template, request, redirect, url_for, flash
from models import Book


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST" and form.validate_on_submit():
        if check_book_exists(form.title.data):
            flash('The book has already existed')
        else:
            new_book = Book(
                title=form.title.data,
                author=form.author.data,
                rating=form.rating.data)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add.html', form=form)


def check_book_exists(name):
    is_exists = Book.query.filter_by(title=name).first()
    if is_exists:
        return True
    return False


@app.route('/edit/<int:book_id>', methods=["GET", "POST"])
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)
    form.sub_btn.label.text = "Update Book"  # change button text
    if request.method == "POST" and form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()  # always remember to commit!!!!!
    return redirect(url_for('home'))
