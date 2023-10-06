from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self._connection = connection

    # I want to keep a list of my shop items with their name and unit price.
    def all(self):
        rows = self._connection.execute("SELECT * FROM items")
        items = [Item(row['id'], row['name'], row['price'], row['quantity']) for row in rows]
        return items

    # I want to know which quantity (a number) I have for each item.
    def quantity_for_item(self, item_name):
        rows = self._connection.execute(
            "SELECT quantity FROM items WHERE name = %s",
            [item_name]
            )
        return rows[0]['quantity']

    # I want to be able to create a new item.
    def create(self, item_name, item_price, item_quantity):
        rows = self._connection.execute(
            "INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s);",
            [item_name, item_price, item_quantity]
            )