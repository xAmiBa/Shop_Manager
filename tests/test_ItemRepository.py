from lib.ItemRepository import ItemRepository
from lib.database_connection import DatabaseConnection
from lib.item import Item

def test_all_items_show(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = ItemRepository(db_connection)
    assert repository.all() == [
        Item(1, 't-shirt', 10, 30),
        Item(2, 'dress', 30, 40),
        Item(3, 'coat', 100, 20)
        ]

def test_quantity_for_dress_40(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = ItemRepository(db_connection)
    test_quantity = repository.quantity_for_item('dress')
    assert test_quantity == 40

def test_new_item_created(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = ItemRepository(db_connection)
    repository.create('hat', 5, 80)
    assert repository.all() == [
        Item(1, 't-shirt', 10, 30),
        Item(2, 'dress', 30, 40),
        Item(3, 'coat', 100, 20),
        Item(4, 'hat', 5, 80)
        ]
    