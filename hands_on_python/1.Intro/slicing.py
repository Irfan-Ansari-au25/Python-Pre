"""
>>> slice[start, end, steps]

string to array 
>>> list(string)

array to string 
>>> ''.join(array)

to reverse string 
>>> string[:: -1]


"""

my_string = "I don't want to die."
my_list = list(my_string)

print(my_list)

new_string = ''.join(my_list)
print(new_string)

print(''.join(my_list[2 : 7 : 1]))

print(my_string[:: -1])



