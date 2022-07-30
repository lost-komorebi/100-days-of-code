#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
import smtplib


class Send_email:

    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.message = f'Low price alert!Only £{flight_data.price} to fly from ' \
                       f'{flight_data.departure_city_name}-{flight_data.departure_airport_iata_code} to ' \
                       f'{flight_data.arrival_city_name}-{flight_data.arrival_airport_iata_code}, from ' \
                       f'{flight_data.outbound_date} to {flight_data.inbound_date}'
        if flight_data.stop_overs != 0:
            self.message += f'\nFlight has 1 stop over, via {flight_data.via_city}'
        self.message += f'\nclick here to book:{flight_data.book_url}'
        #print(self.message)

    def send(self, emails):
        my_email = 'to_fill'
        my_password = 'to_fill'
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=','.join(emails),
                msg=f'subject:cheapest flight\n\n{self.message}'.encode('utf-8'))
