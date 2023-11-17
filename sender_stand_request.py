import configuration
import requests
import data

# Запрос на создание заказа
def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)

# Запрос на получение заказа по треку заказа
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": track_number})