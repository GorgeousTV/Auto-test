# Волков Дмитрий, 19-ая когорта - Финальный проект. Инженер по тестированию плюс
import requests
import data
import config

def test_take_order_is_ok_and_status_code_200():
    create_order = requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                             json=data.create_order_body,
                             headers=data.headers)
    track = create_order.json()['track']
    track = str(track)
    get_order = requests.get(config.URL_SERVICE + config.ORDER_LIST + track,
                            headers=data.headers)
    status_code = get_order.status_code

    assert status_code == 200
