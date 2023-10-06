from lib.item import Item

def test_innit():
    test_item = Item(1, 'Item name', 10, 100)
    assert test_item.id == 1
    assert test_item.name == 'Item name'
    assert test_item.price == 10
    assert test_item.quantity == 100
