class Order():
    def __init__(self, id, customer_name, date):
        self.id = id
        self.customer_name = customer_name
        self.date = str(date)
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Order {self.id} for {self.customer_name} due {self.date}'