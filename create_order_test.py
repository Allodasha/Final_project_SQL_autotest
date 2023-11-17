# Дарья Антонова, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Получение трек номера заказа
def get_track_number():
    track_number = sender_stand_request.post_create_order()
    return track_number.json()["track"]

# Проверка, что код ответа равен 200
def test_create_order():
    track_number = get_track_number()
    get_response = sender_stand_request.get_order(track_number)
    assert get_response.status_code == 200

