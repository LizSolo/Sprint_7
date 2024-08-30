import requests
from data import Urls

class ApiRequests:
    def __init__(self):
        self.base_url = Urls.BASE_URL

    def get(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, json=json)

    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=json)

    def delete(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, json=json)

    def register_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = self.post(Urls.COURIER, json=payload)
        if response.status_code == 201:
            return [login, password, first_name]
        return []

    def login_courier(self, login, password):
        """Метод для выполнения входа курьера и получения его ID."""
        payload = {
            "login": login,
            "password": password
        }
        response = self.post(Urls.COURIER_LOGIN, json=payload)
        if response.status_code == 200 and 'id' in response.json():
            return response.json().get('id')
        return None

    def delete_courier(self, courier_id):
        """Метод для удаления курьера по его ID."""
        endpoint = f"{Urls.COURIER}/{courier_id}"
        response = self.delete(endpoint)
        return response.status_code == 200 and response.json() == {'ok': True}
