#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from flask import Blueprint, jsonify, send_file
import json
from apis import Barcode
import io
from flask_parameter_validation import ValidateParameters, Json
import base64


barcode_bp = Blueprint('barcode', __name__, url_prefix='/barcode')
barcode = Barcode('22a276eb-009e-4cfc-9a6c-2a0a96b5a4f4')


def check_isdigit(string):
    return string.isdigit()


def check_startswith(string):
    return string.startswith('0') or string.startswith('1')


def return_result(response, response_type):
    if response_type == 1:
        return send_file(  # return image directly
            io.BytesIO(response),
            mimetype='image/jpeg'
        )
    elif response_type == 2:
        return str(response)  # return bytes-like string of image
    else:
        return base64.b64encode(response)  # return base64 format of image


@barcode_bp.route('/ean13', methods={'POST'})
@ValidateParameters()
def ean_13(
    value: str = Json(
        min_str_length=12,
        max_str_length=12,
        func=check_isdigit),
        response_type: int = Json(
            min_int=1,
        max_int=3)):
    """Generate a EAN-13 code barcode as PNG file"""
    try:
        response = barcode.generate_ean13(str(value))
    except Exception:
        return jsonify({'error': 'System error, Please try again.'})
    response = eval(response)  # convert bytes-like string to bytes
    return return_result(response, response_type)


@barcode_bp.route('/ean8', methods={'POST'})
@ValidateParameters()
def ean_8(
    value: str = Json(
        min_str_length=7,
        max_str_length=7,
        func=check_isdigit),
        response_type: int = Json(
            min_int=1,
        max_int=3)):
    """Generate a EAN-8 code barcode as PNG file"""
    try:
        response = barcode.generate_ean8(value)
    except Exception:
        return jsonify({'error': 'System error, Please try again.'})
    response = eval(response)  # convert bytes-like string to bytes
    return return_result(response, response_type)


@barcode_bp.route('/qrcode', methods={'POST'})
@ValidateParameters()
def qrcode(
    value: str = Json(
        max_str_length=20),
        response_type: int = Json(
            min_int=1,
        max_int=3)):
    """ Generate a QR code barcode as PNG file """
    try:
        response = barcode.generate_qrcode(value)
    except Exception:
        return jsonify({'error': 'System error, Please try again.'})
    response = eval(response)  # convert bytes-like string to bytes
    return return_result(response, response_type)


@barcode_bp.route('/upca', methods={'POST'})
@ValidateParameters()
def upca(
    value: str = Json(
        min_str_length=11,
        max_str_length=11),
        response_type: int = Json(
            min_int=1,
        max_int=3)):
    """ Generate a UPC-A code barcode as PNG file """
    try:
        response = barcode.generate_upca(value)
    except Exception:
        return jsonify({'error': 'System error, Please try again.'})
    response = eval(response)  # convert bytes-like string to bytes
    return return_result(response, response_type)


@barcode_bp.route('/upce', methods={'POST'})
@ValidateParameters()
def upce(
    value: str = Json(
        min_str_length=7,
        max_str_length=7,
        func=check_startswith),
        response_type: int = Json(
            min_int=1,
        max_int=3)):
    """ Generate a UPC-E code barcode as PNG file """
    try:
        response = barcode.generate_upce(value)
    except Exception:
        return jsonify({'error': 'System error, Please try again.'})
    response = eval(response)  # convert bytes-like string to bytes
    return return_result(response, response_type)


@barcode_bp.route('/product-info', methods={'POST'})
@ValidateParameters()
def get_product_info(
        value: str = Json()):
    """ Lookup EAN barcode value, return product data """
    try:
        response = barcode.return_info_by_barcode(value)
    except Exception:
        return jsonify({'error': 'System error, Please try again.'})
    return json.dumps(response.__dict__)


# @barcode_bp.route('/scan-barcode', methods={'POST'})
# @ValidateParameters()
# def scan_barcode(
#     image: str: Json(func=)
# ):
#     """ Scan and recognize an image of a barcode """
#     try:
#         response = barcode.scan_barcode(image)
#     except Exception:
#         return jsonify({'error': 'System error, Please try again.'})
