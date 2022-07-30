import requests
import datetime as dt
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_iata_by_cityname(self, city_name):
        url = self.url + '/locations/query'
        parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city"
        }
        r = requests.get(url, params=parameters, headers=self.headers)
        r.raise_for_status()
        return r.json()['locations'][0]['code']

    def search_fligt(self, to):
        url = self.url + '/v2/search'

        date_from = (
            dt.datetime.today() +
            dt.timedelta(
                days=1)).strftime("%d/%m/%Y")
        date_to = (
            dt.datetime.today() +
            dt.timedelta(
                days=180)).strftime("%d/%m/%Y")
        parameters = {
            "fly_from": "LON",
            "fly_to": to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 1
        }

        r = requests.get(
            url,
            headers=self.headers,
            params=parameters,
            stream=True)
        data = r.json()
        try:  # 排除找不到航班信息的数据
            data['data'][0]
        except IndexError:
            print(f'No qualified flight found: from LON to {to}')
            return None
        else:
            result = r.json()['data'][0]
            if len(result['route']) == 2:
                flight_data = FlightData(
                    result['price'],
                    result['cityFrom'],
                    result['flyFrom'],
                    result['cityTo'],
                    result['flyTo'],
                    result['route'][0]['local_departure'].split('T')[0],
                    result['route'][1]['local_departure'].split('T')[0],
                    result['deep_link'])
                return flight_data
            else:
                for i in result['route']:
                    if i['cityCodeFrom'] != 'LON' and i['cityCodeFrom'] != to:
                        via_city = i['cityFrom']
                        flight_data = FlightData(
                            result['price'],
                            result['cityFrom'],
                            result['flyFrom'],
                            result['cityTo'],
                            result['flyTo'],
                            result['route'][0]['local_departure'].split('T')[0],
                            result['route'][1]['local_departure'].split('T')[0],
                            result['deep_link'],
                            1,
                            via_city)
                        return flight_data
