
import requests
from configuration import CREATE_ORDER_URL, GET_ORDER_BY_TRACK_URL
from data import ORDER_DATA

# Создание заказа
def create_order():
    response = requests.post(CREATE_ORDER_URL, json=ORDER_DATA)
    return response.json()["track"]

# Получение заказа по треку
def get_order_by_track(track):
    url = f"{GET_ORDER_BY_TRACK_URL}?t={track}"
    response = requests.get(url)
    return response