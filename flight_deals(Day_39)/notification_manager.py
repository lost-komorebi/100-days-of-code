from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight
    # details.

    def __init__(self, flight_date):
        self.flight_date = flight_date
        self.message = f'Low price alert!Only £{flight_date.price} to fly from ' \
                       f'{flight_date.departure_city_name}-{flight_date.departure_airport_iata_code} to ' \
                       f'{flight_date.arrival_city_name}-{flight_date.arrival_airport_iata_code}, from ' \
                       f'{flight_date.outbound_date} to {flight_date.inbound_date}'
        print(self.message)

    def send(self):

        account_sid = 'to_fill'
        auth_token = 'to_fill'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=self.message,
                from_='to_fill',
                to='to_fill'
            )

        print(message.sid)
