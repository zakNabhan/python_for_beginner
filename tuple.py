#A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets.

thistuple = ("apple", "banana",
             "cherry", "orange", "kiwi", "melon",
             "mango")
print(thistuple[1])

# negative Indexing
#Print the last item of the tuple:
print(thistuple[-1])


#range of index
#Return the third, fourth, and fifth item:
print(thistuple[2:5])

#Range of Negative Indexes
#This example returns the items from index -4
# (included) to index -1 (excluded)
print(thistuple[-4:-1])



'''
Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns 
the position of where it was found
'''