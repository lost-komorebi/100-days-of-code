from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight
    # details.

    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.message = f'Low price alert!Only £{flight_data.price} to fly from ' \
                       f'{flight_data.departure_city_name}-{flight_data.departure_airport_iata_code} to ' \
                       f'{flight_data.arrival_city_name}-{flight_data.arrival_airport_iata_code}, from ' \
                       f'{flight_data.outbound_date} to {flight_data.inbound_date}'
        #print(self.message)

    def send(self):

        account_sid = 'ACb3a5126676a80d57cd1e86ddd7492671'
        auth_token = '0466b3b8fd96e4dc9f0b6aaf73725c8e'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=self.message,
                from_='+18434387898',
                to='+840397757552'
            )

        print(message.sid)
