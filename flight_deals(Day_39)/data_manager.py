import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def read_excel(self, sheet):
        url = self.url + '/' + sheet
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        sheet_date = r.json()
        return sheet_date

    def update_excel(self, sheet, id, param):
        url = self.url + '/' + sheet + '/' + str(id)
        data = {
            "price": {"iataCode": param}
        }
        r = requests.put(url=url, json=data, headers=self.headers)
        r.raise_for_status()
        return r.status_code

    def write_excel(self, sheet, data):
        url = self.url + '/' + sheet
        parameters = {
            "user": {
                "firstName": data.first_name,
                "lastName": data.last_name,
                "email": data.email
            }
        }
        r = requests.post(url, headers=self.headers, json=parameters)
        r.raise_for_status()
        return r.status_code
