import pytest
import allure
from data import Urls
from api_requests import ApiRequests
from data import Order

class TestOrder:
    @allure.title("Проверка, что при создании заказа можно выбрать цвет самоката")
    @pytest.mark.parametrize("color", [[], ["BLACK"], ["GREY"]])
    def test_create_order(self, color):
        api_requests = ApiRequests()
        # Копируем словарь заказа и обновляем цвет
        order_data = Order.ORDER.copy()
        order_data["color"] = color

        response = api_requests.post(Urls.ORDER_URL, json=order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
