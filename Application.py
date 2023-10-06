from lib.ItemRepository import ItemRepository
from lib.OrderRepository import OrderRepository
from lib.database_connection import DatabaseConnection

class Application():
    # facilitate connection with postrgeSQL database: shop_manager and seed
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/shop_manager.sql')
        
    def run(self):
        item_repository = ItemRepository(self._connection)
        order_repository = OrderRepository(self._connection)

        print('Welcome to the shop manager program!')

        while True:
            user_choice = input(
                "What do you want to do?\n"\
                    "1 = list all shop items\n"\
                        "2 = create a new item\n"\
                            "3 = list all orders\n"\
                                "4 = create a new order\n"\
                                    "5 = exit program\n"
                                    )
            match user_choice:
                case '1':
                    print(item_repository.all())

                case '2':
                    item_repository.create(input("name of the item: "),
                                                    int(input("price of the item: ")),
                                                        int(input("quantity of the item: "))
                                                        )
                    print(item_repository.all())

                case '3':
                    print(order_repository.all())

                case '4':
                    order_repository.create_order(input("name of the customer: "),
                                                    input("due date (YYYY-MM-DD): ")
                                                    )
                    
                case '5':
                    break

if __name__ == '__main__':
    app = Application()
    app.run()