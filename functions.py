'''
Creating a Function
In Python a function is defined using the def keyword:

'''


def my_function():
    print("Hello from a function")


my_function()


# whit a arguments

def test(fname, lname, age, salary):
    print(fname + "  test")


test('nabhan', '34', '39384', 898)

print("\n________________________-\n")


def test(*args):
    for x in args:
        print(x)
test('nabhan', '34', '39384', 898)


#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



# return a value

def test_2(x, y):
    return x+y
print(test_2(3,4))