from lib.order import Order

def test_innit_order():
    test_order = Order(1, 'Amina Ba', '2022-10-05')
    assert test_order.id == 1
    assert test_order.customer_name == 'Amina Ba'
    assert test_order.date == '2022-10-05'