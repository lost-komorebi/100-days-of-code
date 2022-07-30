# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


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

sheet_date = data_manager.read_excel()

for i in sheet_date['prices']:
    if i['iataCode'] == '':
        iataCode = flight_search.get_iata_by_cityname(i['city'])
        data_manager.update_excel(i['id'], iataCode)
    result = flight_search.search_fligt(i["iataCode"])
    if result and result.price < i['lowestPrice']:
        message = NotificationManager(result)
        message.send()
