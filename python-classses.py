# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor,
# or a "blueprint" for creating objects.

'''
The self parameter is a
reference to the current instance of the class,
 and is used to access variables that belongs to
  the class.

It does not have to be named self , you can call it
 whatever you like, but it has to be
 the first parameter of any function in the class:
'''


# simple form of classe that dont usefull in real life of applications

class Test:
    x = 3


obj = Test()
print(obj.x)

#create a class use built-in init function

class User:
    def __init__(self, name, age, id):
        self.name=name
        self.age=age
        self.id=id

# obeject define
user1 = User('zakaria', 23, 9389)

print(user1.name, user1.age)


class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def salary(self):
        if self.age > 20:
            print("your old is not enough", self.age)
        else:
            print('welcome ' + self.name)
# create an object
emp = Employee('nabhan', 2)
#call the function
emp.salary()

