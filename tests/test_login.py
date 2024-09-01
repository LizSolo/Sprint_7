import allure
from data import Urls, ResponseMessages
from api_requests import ApiRequests
from utils import generate_courier_data

class TestLogin:
    @allure.title("Проверка, что курьер может авторизоваться")
    def test_login_courier(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        api_requests.register_courier(login, password, first_name)
        payload = {
            "login": login,
            "password": password
        }

        response = api_requests.post(Urls.COURIER_LOGIN, json=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title("Проверка, что с несуществующим пользователем, запрос возвращает ошибку")
    def test_login_with_nonexistent_user(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        payload = {
            "login": login,
            "password": password
        }

        response = api_requests.post(Urls.COURIER_LOGIN, json=payload)
        assert response.json() == {'code': 404, 'message': ResponseMessages.ERROR_USER}

    @allure.title("Проверка, что система вернёт ошибку, если неправильно указать логин")
    def test_login_courier_with_nonexistent_login(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        api_requests.register_courier(login, password, first_name)
        payload = {
            "login": f'{login}g',
            "password": password
        }

        response = api_requests.post(Urls.COURIER_LOGIN, json=payload)
        assert response.json() == {'code': 404, 'message': ResponseMessages.ERROR_USER}

    @allure.title("Проверка, что система вернёт ошибку, если неправильно указать пароль")
    def test_login_courier_with_nonexistent_password(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        payload = {
            "login": login,
            "password": f"{password}r"
        }

        response = api_requests.post(Urls.COURIER_LOGIN, json=payload)
        assert response.json() == {'code': 404, 'message': ResponseMessages.ERROR_USER}

    @allure.title("Проверка, что если поля пароль нет, запрос возвращает ошибку")
    def test_login_courier_missing_password(self):
        api_requests = ApiRequests()
        login, password, first_name = generate_courier_data()
        payload = {
            "password": password
        }

        response = api_requests.post(Urls.COURIER_LOGIN, json=payload)
        assert response.json() == {'code': 400, 'message': ResponseMessages.ERROR_DATA}
