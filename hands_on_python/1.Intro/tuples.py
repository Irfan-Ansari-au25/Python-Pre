"""
Tuples are immutable
To be a tuple at least one comma is required between the paranthesis

>>> (1,2,3,4)

"""

# single string in a tuple 

t = ("python")
print(type(t))   # type is string here

t1 = ("python",)
print(type(t1)) # type is tuple here


A= (8,5,6,3)
print(A)

B = (8,5,6,)
print(A,B)

c = A + B
print(c)

a = [1,2,3]
a = tuple(a)
print(a)
for x in a:
    b=[]
    b.append(x+5)
print(b)