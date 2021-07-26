"""
>>> sorted() -- Does not change the original ordering
                but gives a new copy
"""





vowel =['a', 'e', 'i','o' ,'u']
# word = input("provide a word to search for vowels:")
word = "Missippi"
found = []

for letter in word:
    if letter in vowel:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)


my_dict = {"name" : "john",
            "birth_year" : 1997,
            "age": 2037 - 1997}
print(my_dict)


for kv in my_dict:
    print(kv)
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for kv in my_dict.items():
    print(kv)

for value in my_dict:
    print("value is :", my_dict[value])

for k, v in my_dict.items():
    print("key",k , "value", v)

    