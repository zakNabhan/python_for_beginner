class Person:
    id = 0

    #hier we define the arttribut for the person
    # and id that everyone +1
    def __init__(self, name, phone, gender):
        Person.id +=1
        self.id= Person.id
        self.name = name
        self.phone = phone
        self.gender = gender


