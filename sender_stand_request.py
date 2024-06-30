import data
import configuration
import requests


# Создание заказа
def create_order(body):
    return requests.post (configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.BASE_URL}{configuration.ORDER_TRACK_URL}{track_number}"
    response = requests.get(get_order_url)
    return response