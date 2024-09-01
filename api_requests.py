import requests
from data import Urls
import allure

class ApiRequests:
    def __init__(self):
        self.base_url = Urls.BASE_URL

    @allure.step("Отправка GET-запроса на эндпоинт: {endpoint}")
    def get(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, json=json)

    @allure.step("Отправка POST-запроса на эндпоинт: {endpoint}")
    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=json)

    @allure.step("Отправка DELETE-запроса на эндпоинт: {endpoint}")
    def delete(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, json=json)

    @allure.step("Регистрация курьера с логином: {login}")
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
