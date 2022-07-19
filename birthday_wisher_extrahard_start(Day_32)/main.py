##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from datetime import datetime
from random import choice
import smtplib
import pandas as pd
from os import listdir, path


today = datetime.today()
data = pd.read_csv('birthdays.csv')

emails = data[(data.month == today.month) & (
    data.day == today.day)].email.to_list()
recipients = {}
for i in emails:
    recipients[data[data.email == i].name.to_string(index=False)] = i


def send_email(email, letter):
    my_email = 'to_fill'
    my_password = 'to_fill'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=letter)


if recipients:
    for i in recipients:
        folder = 'letter_templates'
        letters = [path.join(folder, f) for f in listdir(folder)]
        letter = choice(letters)
        with open(letter) as f:
            body = f.read().replace('[NAME]', i)
        letter = 'subject:HAPPY BIRTHDAY!\n\n{}'.format(body)
        send_email(recipients[i], letter)
