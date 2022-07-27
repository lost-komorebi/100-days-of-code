#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import requests
import datetime


today = datetime.datetime.today().strftime("%d/%m/%Y")
time = datetime.datetime.today().strftime("%H:%M:%S")


nutri_app_id = 'to_fill'
nutri_app_key = 'to_fill'

nutri_headers = {
    "x-app-id": nutri_app_id,
    "x-app-key": nutri_app_key
}

sheety_headers = {"Authorization": "to_fill"}


def get_info():
    query = input("what exercises did you do today?:")
    params = {
        "query": query,
        "gender": "male",
        "weight_kg": 66.6,
        "height_cm": 170,
        "age": 30
    }
    r = requests.post(
        'https://trackapi.nutritionix.com/v2/natural/exercise',
        headers=nutri_headers,
        json=params)
    r.raise_for_status()
    return r.json()


def write_excel(data):
    url = 'https://api.sheety.co/cd9f6fd4e921072d94032685135d8203/workoutTracking/workouts'
    r = requests.post(url, json=data, headers=sheety_headers)
    return r.status_code


def read_excel():
    excel = requests.get(
        'https://api.sheety.co/cd9f6fd4e921072d94032685135d8203/workoutTracking/workouts',
        headers=sheety_headers)
    return excel.status_code


info = get_info()
for i in info["exercises"]:
    workout = {
        "workout": {
            'date': today,
            'time': time,
            'exercise': i['name'].lower(),
            'duration': i['duration_min'],
            'calories': i['nf_calories'],
        }
    }
    write_excel(workout)
