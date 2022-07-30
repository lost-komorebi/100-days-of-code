# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from user_acquisition import User
from smtp_email import Send_email


sheety_headers = {
    "Authorization": "to_fill"
}
sheety_url = "to_fill"

kiwi_headers = {
    "accept": "application/json",
    "apikey": "to_fill"
}
kiwi_url = "https://tequila-api.kiwi.com"

data_manager = DataManager(sheety_url, sheety_headers)
flight_search = FlightSearch(kiwi_url, kiwi_headers)

sheet_date = data_manager.read_excel('prices')


# first_name = input(
#     "Welcome to Angela's Flight Club.\nWe find the best flight deals and email you.\nWhat is your first name?\n")
# last_name = input("What is your last name?\n")
#
#
# def check_email():
#     email = input("What is your email?\n")
#     email2 = input("Type your email again.\n")
#     if email == email2:
#         user = User(first_name, last_name, email)
#         data_manager.write_excel('users', user)
#     else:
#         check_email()
#
#
# check_email()
emails = [i['email'] for i in data_manager.read_excel('users')['users']]
for i in sheet_date['prices']:
    if i['iataCode'] == '':
        iataCode = flight_search.get_iata_by_cityname(i['city'])
        data_manager.update_excel('prices', i['id'], iataCode)
    result = flight_search.search_fligt(i["iataCode"])
    if result and result.price < i['lowestPrice']:
        email = Send_email(result)
        email.send(emails)
