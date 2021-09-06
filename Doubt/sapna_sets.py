"""



d {
   "a" : [1,3,4,65],
    "b" : [3,4,5,6,7,]
}



"""


d = {
   "a" : [1,3,4,65],
    "b" : [3,4,5,6,7]
}

c = []                  # [[1, 3, 4, 65], [3, 4, 5, 6, 7]]
for k,v in d.items():
    c.append(v)
print(c)

d= []
for i in range(len(c)):
    d += c[i]
print(list(set(d)))