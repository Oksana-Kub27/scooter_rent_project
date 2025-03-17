import requests

# Создание заказа
def create_order():
    url = "https://58b0b985-695f-4c43-8c59-9f180be86f29.serverhub.praktikum-services.ru/api/v1/orders"
    payload = {
        "firstName": "Оксана",
        "lastName": "Кубликова",
        "address": "Москва, ул. Ленина, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2023-10-10",
        "comment": "Позвонить за час до доставки",
        "color": ["BLACK"]
    }
    response = requests.post(url, json=payload)
    return response.json()["track"]

#  Получение заказа по треку
def get_order_by_track(track):
    url = f"https://58b0b985-695f-4c43-8c59-9f180be86f29.serverhub.praktikum-services.ru/api/v1/orders/track?t={track}"
    response = requests.get(url)
    return response

from sender_stand_request import create_order, get_order_by_track

# Проверка кода ответа
def test_order_creation():
    track = create_order()
    response = get_order_by_track(track)
    assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
    print("Тест пройден успешно!")

# Запуск теста
if __name__ == "__main__":
    test_order_creation()
    ##Оксана Кубликова, 27-я когорта — Финальный проект. Инженер по тестированию плюс