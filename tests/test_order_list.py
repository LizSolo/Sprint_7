import allure
from data import Urls
from conftest import api_requests

class TestOrderList:
    @allure.title("Проверка, что в тело ответа на запрос списка возвращается список заказов")
    def test_get_order_list(self, api_requests):
        response = api_requests.get(Urls.ORDER_URL)
        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)