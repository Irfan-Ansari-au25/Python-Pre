
vowels = ['a', 'e', 'i', 'o', 'u']
word = "iliketotravel"
vowel_dict = dict()

for letter in word:
    if letter in vowels:
        # if letter not in vowel_dict:
        #     vowel_dict[letter] = 1
        # else: 
        #     vowel_dict[letter] += 1
        
        vowel_dict.setdefault(letter,0)
        vowel_dict[letter] += 1
for k, v in sorted(vowel_dict.items()):
    print(k, "was found", v, "times")
# print(vowel_dict)

fruits = dict()
#----- USE of setdefault(key,value)
# if 'banana' not in fruits:
#     fruits['banana'] = 1
fruits.setdefault('pears', 0)
fruits['pears'] += 1
print(fruits)
