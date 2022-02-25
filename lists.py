# A list is a collection which is ordered and changeable.
# In Python lists are written with square brackets.

thislist = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6']
#thislist=   [0]   ,  [1]    ,  [2]  , [3]     , [4]
print(thislist)

# access items in the list
print(thislist[1])

# negative indexing
print(thislist[-1])

#Range of Indexes
#You can specify a range of indexes by specifying
#where to start and where to end the range.
print(thislist[2:5])
# its return third fourthm and fifth item

#This example returns the items from the beginning to "test4":

print(thislist[:4])


# change value in list

thislist[2] = "zakaria"
print(thislist)


# loop through a list with for
for x in thislist:
    print(x)


# check if item exists with in keyword

if 'zakaria' in thislist:
    print("yes")
    # print length of the list
    print(len(thislist))
else:
    print('no')

# add a new item to the list with append
# it will be added at the end of the list

thislist.append("nabhan")
print(thislist)

#To add an item at the specified
# index, use the insert() method:
# Insert an item as the second position:
thislist.insert(1, "username")
print(thislist)

# remove item
thislist.remove('test1')
print(thislist)

#The pop() method removes the specified index,
# (or the last item if index is not specified):
thislist.pop()
print(thislist)


#The del keyword removes the specified index:
del thislist[1]
print(thislist)

#The clear() method empties the list:

#Make a copy of a list with the copy() method:
#Make a copy of a list with the list() method
mylist = thislist.copy()
mylist = list(thislist)
print(mylist)



'''
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''



