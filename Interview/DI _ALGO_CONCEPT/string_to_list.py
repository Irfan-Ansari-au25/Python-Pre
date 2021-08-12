"""
The split() method splits a string into a list.
>>> string.split(separator, maxsplit) 

#parameter optional separator ='space" by default
"""

text = 'a,b,c'
text = text.split(',')
print(text)

text2 = '1234'
list1 = []
for i in text2:
    list1.append(int(i))
print(list1)

#Split the string into a list with max 2 items:

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)