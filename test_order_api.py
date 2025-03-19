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
