"""
In programming you often need to know if
 an expression is True or False.

You can evaluate any expression in Python, and
 get one of two answers, True or False.

 When you compare two values, the expression
 is evaluated
 and Python returns the Boolean answer
"""

print(10<3)
print(10>3)
print(10==3)

# print a message

password = 3333
password_2 =3334

if password == password_2:
    print("password match")
else:
    print("dont match")

#Print "YES!" if the function returns True,
# otherwise print "NO!":

def myfunction():
    return True

if myfunction():
    print("yes ! printed")
else:
    print("NO !")


'''
Python verfügt auch über 
viele integrierte Funktionen,
 die einen booleschen Wert zurückgeben,
  z. B. die isinstance() Funktion,
   mit der bestimmt werden kann, 
   ob ein Objekt von einem bestimmten Datentyp ist:
'''
x = 200
print(isinstance(x, str)) # return false, because is x not str
