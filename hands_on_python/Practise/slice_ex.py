
word = "Don't panic!"
wlist = list(word)
print(wlist)

# Technique to swap to element in a list
# string1 = wlist[1:3] + wlist[4:8]
# string1[2], string1[3] = string1[3], string1[2]
# string1[4], string1[5] = string1[5], string1[4]
# print(string1) 
new_phrase = "".join(wlist[1:3])
new_phrase = new_phrase + "".join([wlist[5], wlist[4], wlist[7], wlist[6]])
print(new_phrase)