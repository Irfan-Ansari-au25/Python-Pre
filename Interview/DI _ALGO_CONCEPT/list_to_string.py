"""
The join() method takes all items in an iterable and joins them into one string.
>>> string.join(iterable)



list1 = ['1', '2', '3']
str1 = ''.join(list1)
Or if the list is of integers, convert the elements before joining them.

list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)

"""

list1 = ['1', '2', '3']
str1 = ''.join(list1)
print(str1)


list2 = [1, 2, 3]
str2 = ''.join(str(e) for e in list2)
print(str2)

myTuple = ('1','2','3','4','5')
myList = [1,2,3,4,5]

x = "*".join(myTuple)

y = "#".join(str(i) for i in myList)

print(x)
print(type(x))

print(y, type(y))