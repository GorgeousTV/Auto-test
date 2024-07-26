# Волков Дмитрий, 19-ая когорта - Финальный проект. Инженер по тестированию плюс
import requests
import data
import config

def create_new_order():
    response = requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                             json = data.create_order_body,
                             headers = data.headers)
    track = response.json()['track']
    return str(track)
def take_order():
    response = requests.put(config.URL_SERVICE + config.ORDER_LIST + create_new_order(),
                            headers = data.headers)
    code = response.status_code
    return code
def test_get_order_info():
    response = take_order()
    assert response == 200
