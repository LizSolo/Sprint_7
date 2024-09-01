class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    COURIER = 'api/v1/courier'
    COURIER_LOGIN = f'{COURIER}/login'

    ORDER_URL = 'api/v1/orders'

class Order:
    ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}

class ResponseMessages:
    LOGIN_ERROR ='Этот логин уже используется. Попробуйте другой.'
    OK_MESSAGE = {'ok': True}
    ERROR_USER = 'Учетная запись не найдена'
    ERROR_DATA = 'Недостаточно данных для входа'