"""
>>> list.remove('desired element')
>>> list.pop() -- Remove last element in a list
>>> list.pop('index') -- Remove element at given index
>>> list.extend([])   -- concatenate two lists OR 
>>> list1 + list2 
>>> list.insert(index, value) -- To insert anything 'BEFORE' specific index

"""

number = list()

for i in range(10):
    number.append(i)

print(number)

number.remove(7)
print(number)
# number.remove(12) -- It will throw error

number.pop(5)
print(number)

number.pop()
print(number)

list1 = [1, 2, 3, 4, 5]
list2 = [6,7,8, 9, 10, 11]
list1.extend([7,8,9,10])
print(list1)
print(list1)
list1.insert(4, "Hi there !")
print(list1)
