"""
input : [1,2,3]
output : [1,2,4]

"""


# test = [2,1,3,8]
# out = ''
# output =[]

# for i in test:
#     out += str(i)

# def edge_case():
#     if(int(out) == 0):
#         return ( test[0 : -1] + [1])
#     else:
#         result = int(out) + 1

#         for i in str(result):
#             output.append(int(i))

#         return output


# print(edge_case())






    

num = [1,9,5]

carry = 0

carry = (num[-1] + 1 ) // 10
num[-1] = (num[-1] + 1 ) % 10

print(carry , num)

i = len(num) - 2

while(i >= 0):
    x = (num[i] + carry ) % 10
    carry = (num[i] + carry ) // 10
    print(carry)
    num[i] = x
    i -= 1

if carry > 0 :
    num.insert(0,carry)
print(num)