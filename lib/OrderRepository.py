from lib.order import Order

class OrderRepository():
    def __init__(self, connection):
        self._connection = connection

# I want to keep a list of orders with their customer name.
    def all(self):
        rows = self._connection.execute("SELECT * FROM orders;")
        orders = [Order(row['id'], row['customer_name'], row['date']) for row in rows]
        return orders
    
# I want to know on which date an order was placed. 
    def date_for_order(self, order_name):
        # user can choose to search with order name or id
        rows = self._connection.execute("SELECT * FROM orders WHERE customer_name = %s;",
                                        [order_name])
        order_date = rows[0]['date']
        return order_date

# I want to be able to create a new order.
    def create_order(self, order_name, date):
        self._connection.execute(
            "INSERT INTO orders (customer_name, date) VALUES (%s, %s);",
            [order_name, date]
            )
        

# I want to assign each order to their corresponding item.
    def add_item_to_order(self, order_id, item_id):
        self._connection.execute(
            "INSERT INTO items_orders (order_id, item_id) VALUES (%s, %s);",
            [order_id, item_id]
            )  

