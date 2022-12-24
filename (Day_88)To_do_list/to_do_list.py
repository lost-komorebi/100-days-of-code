#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Blueprint, render_template, redirect, url_for, flash, abort
from forms import AddToDoListForm
from models import ToDoList
from flask_login import current_user, login_required
from models import db


to_do_list_bp = Blueprint('to_do_list', __name__)


@to_do_list_bp.route('/lists', methods=["GET", "POST"])
def get_all_to_do_lists():
    user_id = current_user.get_id()
    all_lists = ToDoList.query.filter_by(
        is_delete=0, user_id=user_id).order_by(
        ToDoList.create_time.desc()).all()
    tdl_form = AddToDoListForm()
    if tdl_form.validate_on_submit():
        if current_user.is_authenticated:
            detail = tdl_form.detail.data
            due_date = tdl_form.due_date.data
            new_tdl = ToDoList(user=current_user,
                               detail=detail,
                               due_date=due_date)
            try:
                db.session.add(new_tdl)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            else:
                return redirect(url_for('to_do_list.get_all_to_do_lists'))
        flash("Please login in.")
        return redirect(url_for('auth.login'))
    return render_template(
        'to_do_list/to_do_list.html',
        lists=all_lists,
        form=tdl_form)


@to_do_list_bp.route('/finish/<int:tdl_id>', methods=["GET"])
@login_required
def finish(tdl_id):
    tdl_to_finish = get_to_do_list(tdl_id)
    if tdl_to_finish:
        if current_user == tdl_to_finish.user:
            tdl_to_finish.status *= -1
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            else:
                return redirect(url_for('to_do_list.get_all_to_do_lists'))
        else:
            flash('You cannot finish this to do list!')
    else:
        flash('Invalid to do list!')


@to_do_list_bp.route('/delete/<int:tdl_id>', methods=["GET"])
@login_required
def delete(tdl_id):
    tdl_to_delete = get_to_do_list(tdl_id)
    if tdl_to_delete:
        if current_user == tdl_to_delete.user:
            tdl_to_delete.is_delete = 1
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            else:
                return redirect(url_for('to_do_list.get_all_to_do_lists'))
        else:
            flash('You cannot delete this to do list!')
    else:
        flash('Invalid to do list!')


def get_to_do_list(tdl_id):
    return ToDoList.query.filter_by(
        id=tdl_id, is_delete=0).first()  # filter_by multiple
