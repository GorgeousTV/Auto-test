# Волков Дмитрий, 19-ая когорта - Финальный проект. Инженер по тестированию плюс

import requests
import config
import data

def create_new_order():
    response = requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                             json = data.create_order_body,
                             headers = data.headers)
    track = response.json()['track']
    return str(track)

def take_order():
    response = requests.get(config.URL_SERVICE + config.ORDER_LIST + create_new_order(),
                            headers = data.headers)
    aboba = response.status_code
    return aboba