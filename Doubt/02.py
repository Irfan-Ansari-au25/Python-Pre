"""
Q3. Write a function which will take a str as input and will return a string
where vowels are removed. (Medium) (5 marks)
Str = ABCDEFG
Result = BCDFG
"""

word = "ABCDEFG"
vowel = "AaEeIiOoUu"
result = ''


for ch in word: #[A B C D E F G ]
    if ch in vowel:
        pass
    else:
        result += ch
print(result)
        


