#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException


class Barcode:

    def __init__(self, key):
        self.key = key
        # Configure API key authorization: Apikey
        self.configuration = cloudmersive_barcode_api_client.Configuration()
        self.configuration.api_key['Apikey'] = self.key
        # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
        # self.configuration.api_key_prefix['Apikey'] = 'Bearer'

    def generate_ean13(self, value):
        # create an instance of the API class
        api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Generate a EAN-13 code barcode as PNG file
            api_response = api_instance.generate_barcode_ean13(value)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling GenerateBarcodeApi->generate_barcode_ean13: %s\n" %
                e)

    def generate_ean8(self, value):
        # create an instance of the API class
        api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Generate a EAN-8 code barcode as PNG file
            api_response = api_instance.generate_barcode_ean8(value)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling GenerateBarcodeApi->generate_barcode_ean8: %s\n" %
                e)

    def generate_qrcode(self, value):
        # create an instance of the API class
        api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Generate a QR code barcode as PNG file
            api_response = api_instance.generate_barcode_qr_code(value)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling GenerateBarcodeApi->generate_barcode_qr_code: %s\n" %
                e)

    def generate_upca(self, value):
        # create an instance of the API class
        api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Generate a UPC-A code barcode as PNG file
            api_response = api_instance.generate_barcode_upca(value)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling GenerateBarcodeApi->generate_barcode_upca: %s\n" %
                e)

    def generate_upce(self, value):
        # create an instance of the API class
        api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Generate a UPC-E code barcode as PNG file
            api_response = api_instance.generate_barcode_upce(value)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling GenerateBarcodeApi->generate_barcode_upce: %s\n" %
                e)

    def return_info_by_barcode(self, value):
        # create an instance of the API class
        api_instance = cloudmersive_barcode_api_client.BarcodeLookupApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Lookup EAN barcode value, return product data
            api_response = api_instance.barcode_lookup_ean_lookup(value)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling BarcodeLookupApi->barcode_lookup_ean_lookup: %s\n" %
                e)

    def scan_barcode(self, image_file):
        api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(
            cloudmersive_barcode_api_client.ApiClient(self.configuration))
        try:
            # Scan and recognize an image of a barcode
            api_response = api_instance.barcode_scan_image(image_file)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling BarcodeScanApi->barcode_scan_image: %s\n" %
                e)
