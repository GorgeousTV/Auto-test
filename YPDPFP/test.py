# Волков Дмитрий, 19-ая когорта - Финальный проект. Инженер по тестированию плюс

import send_request

def test_get_order_info():
    response = send_request.take_order()
    assert response.status_code == 200
