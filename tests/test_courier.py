import allure
from data import Urls, ResponseMessages
from api_requests import ApiRequests
from utils import generate_courier_data

class TestCourier:
    @allure.title("Проверка создания курьера")
    def test_add_courier(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # Отправляем запрос на добавление курьера
        response = api_requests.post(Urls.COURIER, json=payload)
        assert response.status_code == 201
        assert response.json() == ResponseMessages.OK_MESSAGE

    @allure.title("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_add_courier_with_existing_login(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        api_requests.register_courier(login, password, first_name)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Попробуем снова добавить курьера с теми же данными
        response = api_requests.post(Urls.COURIER, json=payload)
        assert response.json() == {'code': 409, 'message': ResponseMessages.LOGIN_ERROR}
