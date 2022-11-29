#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
    flash)
from models import Cafe
from forms import CafeForm
from app import db


cafe_bp = Blueprint('cafe', __name__)


@cafe_bp.route('/')
def index():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)


@cafe_bp.route('/add-cafe', methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        if get_cafe_by_name(cafe_form.name.data):
            flash('Invalid Cafe Name')
        else:
            cafe = Cafe(
                name=cafe_form.name.data,
                map_url=cafe_form.map_url.data,
                img_url=cafe_form.img_url.data,
                location=cafe_form.location.data,
                has_sockets=cafe_form.has_sockets.data,
                has_toilet=cafe_form.has_toilet.data,
                has_wifi=cafe_form.has_wifi.data,
                can_take_calls=cafe_form.can_take_calls.data,
                seats=cafe_form.seats.data,
                coffee_price=cafe_form.coffee_price.data
            )
            try:
                db.session.add(cafe)
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise
            return redirect(url_for('cafe.index'))
    return render_template('add-cafe.html', form=cafe_form)


@cafe_bp.route('/delete/<int:id>')
def delete(id):
    cafe_to_delete = Cafe.query.get_or_404(id)
    try:
        db.session.delete(cafe_to_delete)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    return redirect(url_for('cafe.index'))


def get_cafe_by_name(name):
    cafe = Cafe.query.filter_by(name=name).first()
    if cafe:
        return True
    return False
