#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    flash, send_from_directory)
import os
from werkzeug.utils import secure_filename
from forms import PdfForm
from PyPDF2 import PdfReader
from tts import tts

tts_bp = Blueprint('text_to_speech', __name__)

UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
    """ check file extension """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@tts_bp.route('/', methods=['GET', 'POST'])
def index():
    """ file upload """
    form = PdfForm()
    if form.validate_on_submit():
        f = form.pdf.data
        filename = secure_filename(f.filename)
        if allowed_file(filename):
            f.save(os.path.join(UPLOAD_FOLDER, filename))
            convert(filename)
        else:
            flash('Not support file type')
    return render_template('index.html', form=form)


@tts_bp.route('/convert/<filename>', methods=['GET', 'POST'])
def convert(filename):
    """ convert text to speech """
    output_filename = filename.split('.')[0] + '.mp3'
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)
    text = PdfReader(  # extract text from pdf
        os.path.join(
            UPLOAD_FOLDER,
            filename)).pages[0].extract_text()
    try:
        # call google cloud api to convert text to speech
        tts(text, output_path)
        return redirect(url_for('text_to_speech.finish'))
    except Exception as e:
        print(e)
        flash('System error! Please try again!')


@tts_bp.route('/finish')
def finish():
    return render_template('finish.html')


@tts_bp.route('/upload/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)
