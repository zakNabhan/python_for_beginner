from oop.company.Client import Client
from oop.company.Employee import Employee


class Company:
    persons = []
    products = []
    orders = []

    # define add products functione

    def add_product(self, product):
        self.products.append(product)

    # define add person
    def add_person(self, person):
        self.persons.append(person)

    # define add Order
    def add_order(self, order):
        self.orders.append(order)

    # define remove product function

    def remove_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print("Product-", id, "wurde gelosche")
            else:
                print("product id ist not found")

    def remove_person(self, id):
        for person in self.persons:
            if person.id == id:
                self.persons.remove(person)
            print("es wurde gelöscht", person.id)
        else:
            print("not found")

    def remove_oder(self, id):
        for order in self.orders:
            if order.id == id:
                self.orders.remove(order)
                print("order gelsöcht")
            else:
                print("order not founded")

    def print_person_info(self, id):
        for person in self.persons:
            if person.id == id:
                print("person with id", id)
                print("name", person.name)
                print("phone", person.phone)
                print("gender", person.gender)

                if isinstance(person, Client):
                    print("email", person.email)
                elif isinstance(person, Employee):
                    print("salary", person.salary)
                    print("working_time", person.working_time)
            else:
                print("person is not founded")

    def print_product_details(self, id):
        for product in self.products:
            if product.id == id:
                print("Product with id", id, "info.")
                print("Name:", product.name)
                print("Price:", str(product.price) + "$")
                print("----------------------")
            else:
                print("product is not founded")

    def print_order_details(self, id):
        total_sum = 0
        for order in self.orders:
            if order.id == id:
                print("id order", id)
                print("datum: ", order.date)
                print("Is bezahlt:", "yes " if order.is_paid else "no")
                print("ordered by .", order.person.name)
                print("products")

                for product in self.products:
                    total_sum += product.price
                    print("-" + product.name + ": " + str(product.price) + "$")
                print("total price: " + str(total_sum))

            else:
                print("not founded")

    def print_person_orders(self, id):
        is_person_exist = False

        for person in self.persons:
            if person.id == id:
                is_person_exist = True
                break
        if not is_person_exist:
            print("person- not founded")

        print("alle orders", id)

        for order in self.orders:
            if order.person.id == id:
                print("> Order: #" + str(order.id))
                print("  Date:", order.date)
                print("  Is paid:", "yes" if order.is_paid else "no")
                print("  Ordered by:", order.person.name)
                print("  Products")

                total_sum = 0
                for product in order.products:
                    total_sum += product.price
                    print("  - " + product.name + ": " + str(product.price) + "$")
                print("  Total Price: " + str(total_sum) + "$")
            print("----------------------")
