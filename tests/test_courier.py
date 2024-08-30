import allure
from conftest import api_requests,courier_data
from data import Urls, ResponseMessages

class TestCourier:
    @allure.title("Проверка создания курьера")
    def test_add_courier(self, api_requests, courier_data):
        login, password, first_name = courier_data
        # Определяем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # Отправляем запрос на добавление курьера
        response = api_requests.post(Urls.COURIER, json=payload)
        # Проверяем, что статус код ответа 201 и тело ответа содержит {'ok': True}
        assert response.status_code == 201
        assert response.json() == ResponseMessages.OK_MESSAGE

        courier_id = api_requests.login_courier(login, password)
        api_requests.delete_courier(courier_id)

    @allure.title("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_add_courier_with_existing_login(self, api_requests, courier_data):
        login, password, first_name = courier_data
        api_requests.register_courier(login, password, first_name)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Попробуем снова добавить курьера с теми же данными
        response = api_requests.post(Urls.COURIER, json=payload)
        assert response.json() == {'code': 409, 'message': ResponseMessages.LOGIN_ERROR}
