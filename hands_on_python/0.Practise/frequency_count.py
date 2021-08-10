list = ['a', 'b', 'c','a']
# for i in range(len(list)):
#     print('hello',list[i])
dictA = {}
for i in list:
    if i in dictA:
        dictA[i] +=1
    else:
        dictA[i] = 1
print(dictA)