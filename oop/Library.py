class Library:

    authors = []
    books = []

    def add_author(self, author):
        self.authors.append(author)

    def remove_author(self, id):
        for author in self.authors:
            if author.id == id:
                self.authors.remove(author)
                return
        print("author with id", id, "is not found")
        print("_______________")

    def  print_author(self, id):
        for author in self.authors:
            if author.id == id:
                print("Author with id", id, "info.")
                print("Name:", author.name)
                print("Phone:", author.phone)
                print("Email", author.email)
                print("----------------------")
                return
        print("author with id", id, "is not found")
        print("_______________")

    def print_author_books(self, id):
        is_author_exist = False
        author_name = ""
        for author in self.authors:
            if author.id == id:
                is_author_exist = True
                author_name = author.name
                break
        if not is_author_exist:
            print("Author with id", id, "is not found!")
            print("----------------------")
            return
        print("Books of author " + author_name + ":")

        for book in self.books:
            if book.author.id == id:
                print("- " + book.title)
            print("----------------------")

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return
        print("Book with id", id, "is not found!")
        print("----------------------")

    def print_book(self, id):
        for book in self.books:
            if book.id == id:
                print("Book with id", id, " info.")
                print("Title:", book.title)
                print("Publishing date:", book.publishing_date)
                print("Author:", book.author.name)
                print("----------------------")
                return
        print("Book with id", id, "is not found!")
        print("----------------------")














