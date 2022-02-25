class Order:
    id = 0
    def __init__(self, date, is_paid, person, products):
        Order.id +=1
        self.id = Order.id
        self.date = date
        self.is_paid =is_paid
        self.person = person
        self.products = products
