'''

Inheritance allows us to define a class that
inherits all the methods and properties from
 another class.

Parent class is the class being inherited from,
also called base class.

Child class is the class that inherits
from another class, also called derived class.

'''

class User:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def printdata(self):
        print('my Data: \n', self.fname, self.lname)
#Use the User class to create an object,
# and then execute the printdata method:
user1 = User('zakaria', 'nabhan')
user1.printdata()

class Admin(User):
    pass

admin = Admin('captiq', "test")
admin.printdata()


class Employee(User):
    def __init__(self, fname, lname):
        User.__init__(self, fname, lname)

x = Employee("Max", "twe")
x.printdata()


class Student(User):
    def __init__(self, fname, lname, degree):
        super().__init__(fname, lname)
        self.degree=degree
    def welcome(self):
        print(self.lname, self.fname, self.degree)

x = Student("Atta", "twe", 2.3)
x.printdata()
x.welcome()
