from oop.Author import *
from oop.Book import Book
from oop.Library import Library

author1 = Author("Mhamad", "+96170123456", "mhamad@gmail.com")
author2 = Author("Salem",  "+9664021833",  "salem@gmail.com")
author3 = Author("Rola",   "+9631249392",  "rola@gmail.com")

book1 = Book("Learn Java", "12-20-2019", 1, author1)
book2 = Book("Learn HTML", "8-5-2018", 3, author1)
book3 = Book("PHP for beginners", "10-2-2019", 1, author2)
book4 = Book("C# for dummies", "12-20-2019", 1, author3)

library = Library()

library.add_author(author1)
library.add_author(author2)
library.add_author(author3)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.print_author(1)
library.print_author(2)
library.print_author(3)

library.print_book(1)
library.print_book(2)
library.print_book(3)
library.print_book(4)
'''
library.print_author_books(1)
library.print_author_books(2)
library.print_author_books(3)

library.remove_author(2)
library.print_author(2)
library.print_author_books(2)'''