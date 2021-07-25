
vowel = ["a", 'i', 'e', 'o', 'u']

# word = input("please enter a word:")
word = "Millenotes"
vowel_num =dict()
found = list()


for letter in word:
    if letter in vowel:
        if letter not in found:
            found.append(letter)

    if letter not in vowel_num :
        vowel_num[letter] = 1
    else:
        vowel_num[letter] += 1
print(vowel_num)
print(found)