"""
left shift : 
>>> 3 << 1 ( 3 * 2 )
>>> 3 << 2 ( 3 ** 2 )

right shift :
>>> 40 >> 1 (40 // 2)
>>> 40 >> 2 (40 // 2 ** 2)

================================================================

operators:

>>> 2 & 3   AND
>>> 3 | 5   OR
>>> 3 ^ 0   NOR
>>> 2 ^ 2 ^ 3 ^ 4 ^ 4 ^ 5 ^ 5 (3)
>>> 0 ^ something => something

"""


num = [1,1,2,2,3,3,9,4,4,5,5,6,6]

# ans = dict()

# for i in num:
#     if i not in ans:
#         ans[i] = 1
#     else:
#         ans[i] += 1

# print(ans)
# time complexity O(n)
# space complexity O(n)

ans = num[0]
for i in range(len(num)-1):
    ans = ans ^ num[i + 1]

print(ans)

# time complexity O(n)
# space complexity O(1)
