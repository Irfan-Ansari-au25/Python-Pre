"""
str = "Hello this is me"
out = "me is this Hello"


"""
# def reverse_words(name):
    
#     word_list = name.split(" ")
#     word_list = word_list[::-1]

#     return word_list
# print(reverse_words("Hello this is me"))

name = "i am manirul islam "

string = ""
words = []

for ch in name:
    if (ch != " "):
        string += ch
    if(ch == " " or ch == name[len(name)-1]):
        words.append(string)
        string = ""

words = words[::-1]
# print(words)

res =""
for word in words :
    res += word + " "


print(res)


