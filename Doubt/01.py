"""

Q-1 )Write a program to print the vowels in a particular str given by the
user. (5 marks)
Eg Attainu Output: vowels are A, a, i, u

"""

my_string = input('Enter a string : ')

vowel = 'AaEeIiOoUu'


for ch in my_string: # [ch = a]
    if ch in vowel:
        print(ch)

#pythontutor.com


