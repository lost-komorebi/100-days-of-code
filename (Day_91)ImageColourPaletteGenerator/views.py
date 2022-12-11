#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    send_from_directory)
from forms import ImgForm
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
import pandas as pd

SUPPORT_EXTENSIONS = ['jpg', 'png', 'jpeg']
UPLOAD_FILE = 'UPLOAD'
convert_dict = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}

image_bp = Blueprint('image', __name__)


def check_extension(filename):
    if '.' in filename and filename.rsplit(
            '.', 1)[1].lower() in SUPPORT_EXTENSIONS:
        return True


@image_bp.route('/', methods=["GET", "POST"])
def index():
    form = ImgForm()
    if form.validate_on_submit():
        img = form.img.data
        filename = secure_filename(img.filename)
        if check_extension(filename):
            img.save(os.path.join(UPLOAD_FILE, filename))
            colors = color_extract(os.path.join(UPLOAD_FILE, filename))
            return render_template(
                'index.html',
                form=form,
                filename=filename,
                colors=colors)
        else:
            flash('unsupported file')
    else:
        default_file = 'demo.jpg'  # add default demo
        default_path = 'static'
        colors = color_extract(os.path.join(default_path, default_file))
        return render_template(
            'index.html',
            form=form,
            filename=default_file,
            colors=colors)


def color_extract(file, num=10):
    """ extract top num common rgb from pic """
    img = Image.open(file)
    img_array = np.array(img)
    img_as = img_array.shape
    img_array_list = img_array.reshape(img_as[0] * img_as[1], img_as[2])
    top_list = []
    for i in (pd.DataFrame(img_array_list).value_counts(
            normalize=True).head(num).iteritems()):
        top_list.append([rbg_to_hex(i[0]), i[1]*100])
    return top_list


def rbg_to_hex(rgb):
    """ convert rbg to hex"""
    str_hex = '#'
    for i in rgb:
        str_hex += convert_dict[str(i // 16)]
        str_hex += convert_dict[str(i % 16)]
    return str_hex


@image_bp.route('/upload/<filename>')
def display(filename):
    return send_from_directory(UPLOAD_FILE, filename)
