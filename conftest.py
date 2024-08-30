import pytest
from api_requests import ApiRequests
from utils import generate_courier_data

@pytest.fixture
def api_requests():
    return ApiRequests()

@pytest.fixture
def courier_data():
    return generate_courier_data()
