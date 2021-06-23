num = [1,2,2,4,4,4,4,5,5,7,7,7,8,9,9,9,9,9,6]
count = {}

for i in num:
    if i in count.keys():
        count[i] = count[i] + 1
    else:
        count[i] = 1
print(count)
