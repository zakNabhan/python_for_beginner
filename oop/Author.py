class Author:
    id_incrementer = 0
    def __init__(self, name, phone, email):
        Author.id_incrementer +=1
        self.id=Author.id_incrementer
        self.name=name
        self.phone=phone
        self.email=email


