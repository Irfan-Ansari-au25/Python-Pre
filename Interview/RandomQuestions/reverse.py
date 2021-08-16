
num = 12345
num_list  = list()
# def same(num):
while num > 0 :
    rem = num % 10
    num_list.append(rem)
    num = num // 10
num_list.reverse()

x = ''
print(num_list)
for u in num_list :
    x += str(u)
num2 = int(''.join(list(x)))
print(num2,type(num2))
print(num, type(num))
print(12345 == num2)
# same(num)
print(num)

    