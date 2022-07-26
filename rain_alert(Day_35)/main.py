#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""get a sms alert if it rains in the next 12 hours"""

from twilio.rest import Client
__author__ = 'komorebi'

import requests
import os
os.environ['TWILIO_ACCOUNT_SID'] = 'to_fill'
os.environ['TWILIO_AUTH_TOKEN'] = 'to_fill'

api_key = 'to_fill'
my_lat = -34.603683
my_lon = -58.381557
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
r = requests.get(
    'https://api.openweathermap.org/data/2.5/onecall',
    params=parameters)
r.raise_for_status()
data = r.json()['hourly'][0:12]


for i in data:
    for _ in i['weather']:
        if _['id'] < 7000:
            print('bring an umbrella')
            message = client.messages \
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='to_fill',
                    to='to_fill'
                )

            print(message.sid)
    break
