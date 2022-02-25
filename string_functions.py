"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value

"""

"""
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and
 returns the position of where it was found
format(), format_map()		Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

# Die strip() Methode entfernt Lerrzeichen vom Anfang
# oder vom Ende

a = " today is, saturday! "
print(a.strip())


# lower() zu kleinbuchenstaben

a = "NABHAN, ZAKARIA"
print(a.lower())

# upper() zu großen Buchstaben
a = "nabhan, zakaria"
print(a.upper())

#replace() ersetzt eine Zeichenfolge durch eine andere Zeichenfolge
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# String überprüfen

x = "username is wrong"
y = "ixcs" in x
print(y)

x = "username is wrong"
y = "ixcs" not in x
print(y)

# Die format()Methode nimmt die übergebenen Argumente,
# formatiert sie und platziert sie in der Zeichenfolge,
# in der sich die Platzhalter {}befinden:

password = 439749
login = "my password : {}"
print(login.format(password))

password_1= 34909
user_nam= "admin"
email  = "test@captiq.com"

my_login_data= "Login-Data: {}, {}, {}"

print(my_login_data.format(password_1, user_nam, email))



