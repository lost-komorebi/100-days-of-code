import smtplib
import datetime as dt
import random

day = dt.datetime.today()

if day.weekday() in range(0, 5):  # only send email on weekdays

    with open('quotes.txt') as f:
        r = f.readlines()
    body = random.choice(r)

    my_email = 'to_fill'
    my_password = 'to_fill'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='codeof100days@yahoo.com',
            msg='subject:hello\n\nToday is {}.{}'.format(
                # strftime('%A') get weekday as locale’s full name like
                # Sunday,Monday
                day.strftime('%A'),
                body))
