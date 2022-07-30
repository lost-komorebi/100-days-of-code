import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def read_excel(self):
        r = requests.get(self.url, headers=self.headers)
        r.raise_for_status()
        sheet_date = r.json()
        return sheet_date

    def update_excel(self, id, iata):
        url = self.url + '/' + str(id)
        data = {
            "price": {"iataCode": iata}
        }
        r = requests.put(url=url, json=data, headers=self.headers)
        r.raise_for_status()
        return r.status_code
