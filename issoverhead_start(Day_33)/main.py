# Your position is within +5 or -5 degrees of the ISS position.
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

import requests
from datetime import datetime
import time

MY_LAT = 35.689487  # Tokyo
MY_LONG = 139.691711  # Tokyo


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_longitude - 5 < MY_LONG < iss_longitude + \
            5 and iss_latitude < MY_LAT < iss_latitude + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour
    if sunset < time_now < sunrise:
        return True


def send_email():
    my_email = 'to_fill'
    my_password = 'to_fill'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='codeof100days@yahoo.com',
            msg='subject:get up and see the iss\n\nget up and see the iss')


while True:
    if is_overhead() and is_dark():
        send_email()
    time.sleep(60)
