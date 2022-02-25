class Book:
    id_increment = 0
    def __init__(self, title, publishing_date, version, author):
        Book.id_increment +=1
        self.id=Book.id_increment
        self.title=title
        self.publishing_date=publishing_date
        self.version=version
        self.author=author
