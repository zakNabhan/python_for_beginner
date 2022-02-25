'''
Dictionary
A dictionary is a collection which is
unordered, changeable and indexed.
In Python dictionaries are written with curly brackets,
 and they have keys and values.

'''

#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#accessing items

x = thisdict['year']
print(x)
# or with get
y = thisdict.get('model')
print(y)

# change value
thisdict['year'] = 2020
print(thisdict)
print("'''''''''''''''''''''''")


#Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)
print("'''''''''''''''''''''''")

#Print all key and value names in the dictionary, one by one:

for x, y in thisdict.items():
    print(x, y)

print("'''''''''''''''''''''''")
#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
#You can also use the values()
# method to return values of a dictionary:
print("'''''''''''''''''''''''")
for x in thisdict.values():
  print(x)
# removing items
#The popitem() method removes the last inserted item
thisdict.pop("model")
print(thisdict)


print("\n___________________________________________\n")
#nested Dictionaries
#A dictionary can also contain many dictionaries,
# this is called nested dictionaries.

#Create a dictionary that contain three dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)



'''
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''

