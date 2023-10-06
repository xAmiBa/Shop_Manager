from lib.OrderRepository import OrderRepository
from lib.database_connection import DatabaseConnection
from lib.order import Order
from datetime import date

def test_all_orders_listed(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)
    # print(repository.all())
    # print([
    #     Order(1, 'Amina', '2011-11-11'),
    #     Order(2, 'Jack', '2022-02-22')
    # ])
    assert repository.all() == [
        Order(1, 'Amina', '2011-11-11'),
        Order(2, 'Jack', '2022-02-22')
    ]

def test_get_date_for_order_2011_11_11(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)
    assert repository.date_for_order('Amina') == date(2011, 11, 11)

def test_new_order_created(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)  
    repository.create_order('Joe', '2033-03-03')
    assert repository.all() == [
        Order(1, 'Amina', '2011-11-11'),
        Order(2, 'Jack', '2022-02-22'),
        Order(3, 'Joe', '2033-03-03')
        ]
    
def test_new_item_assigned_to_order(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)
    repository.add_item_to_order(2, 3) # order, item

    # retrieve items_orders table
    rows = db_connection.execute("SELECT (order_id, item_id) FROM items_orders WHERE order_id = 2")
    print(rows)
    items_orders = [row['row'] for row in rows]
    assert items_orders == [
        ('2', '1'),
        ('2', '3')
        ]