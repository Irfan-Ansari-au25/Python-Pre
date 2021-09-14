"""
Enumerates returns (index,value) 

"""

A = [1, 4, 1, 4, 1]
B = []

for i,v in enumerate(A):
    # print(i,v)
    B.append((i,v))
print(B)