from oop.company.Company import Company
from oop.company.Employee import Employee
from  oop.company.Person import Person
from oop.company.Product import Product
from oop.company.Order import Order
from oop.company.Company import Client



 
person1 = Client("Mhamad", "+96170123456", "Male", "mhamad@example.com")
person2 = Employee("Nadine", "+9631249392", "Female", 800, "8:00 AM to 3:00 PM")
 
product1 = Product("Keyboard", 15)
product2 = Product("Camera", 45)
product3 = Product("HDD 1TB", 70)
product4 = Product("SSD 1TB", 274.66)
product5 = Product("Mouse", 8)
product6 = Product("Table", 44.55)
 
 
order1 = Order("2020-1-1", True, person1, [product1, product2, product3])
order2 = Order("2020-2-7", True, person1, [product4])
order3 = Order("2020-5-4", False, person2, [product5, product6])
 
company = Company()
 
company.add_person(person1)
company.add_person(person2)
 
company.add_product(product1)
company.add_product(product2)
company.add_product(product3)
company.add_product(product4)
company.add_product(product5)
company.add_product(product6)
 
company.add_order(order1)
company.add_order(order2)
company.add_order(order3)
 
 
company.print_person_info(1)
company.print_person_info(2)
 
 
company.print_product_details(1)
company.print_product_details(2)
company.print_product_details(3)
company.print_product_details(4)
company.print_product_details(5)
company.print_product_details(6)
 
company.print_person_orders(1)
company.print_person_orders(2)
 
 
 

company.print_order_details(1)
company.print_person_orders(1)
