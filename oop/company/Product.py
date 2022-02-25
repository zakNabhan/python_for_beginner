class Product:
    id = 0
    def __init__(self, name, price):
        Product.id+=1
        self.id = Product.id
        self.name = name
        self.price = price
