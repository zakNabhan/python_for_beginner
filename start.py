# learn with examples


print("hallo world")

target_of_python="""
Webentwicklung
Softwareentwicklung
Mathematik
System-Scriptig
KI
Ml
DL
Big Data
"""

print(target_of_python)

# zuweisen mehrerer Variablen in einer Zeile
x, y, z = "test_1", "test_2", "test_3"
print(x)
print(y)
print(z)

#zuweisen mehreren Variablen in einer Zeile denselben Wert:

x = y = z = "denselben Wert"
print(x, z,y)

#Erstellen einer Variable auserhalb der Funktion
#und verwenden Sie innerhalb der Funktion

x = "user_name"

def myfunktion():
    print("nabhan is " + x)
myfunktion()


x = "password"

def auth():
    #global variable is the output
    x = "1234"
    print("is "+ x)
auth()
print(x)


# verwenden von global Schlüssel Wort
x = "awesome"
def test():
    global x
    x = "fantastic"

test()
print("python is "+ x)


# Es kann vorkommen, dass man einen Type für eine Variable
#angeben möchte, Dies kann mir Casting erfolgen

# int(), float(), str()
# beispiel x = int(43)