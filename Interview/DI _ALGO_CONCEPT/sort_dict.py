# sort a dictionary
dic = {-1: 1, 1: 3, -6: 2, 4: 2, 5: 1}
b= dict(sorted(dic.items(), key=lambda item: item[1]))
print(b)