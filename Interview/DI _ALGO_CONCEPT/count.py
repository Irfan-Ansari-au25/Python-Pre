"""
list.count(value)

"""
A = [1, 2, 3, 4, 1, 4, 1]
count1 = A.count(1)
print(count1)
count4 = A.count(4)
print(count4)

b = [i for i in A if A.count(i) > 1]
print(b) 