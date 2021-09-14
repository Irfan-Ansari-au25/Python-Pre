


"""
# n = 3
# l = [1,2,3]

n = int(input())
l = list(map(int,input().split()))
ans = ''
sum = 0
for i in range(n):
    sum += l[i]
    ans += (str(sum)) + ' '
print(ans)
# x = " ".join(ans)
# print(x)

"""

# n = int(input("lenght of list "))
# nums = list(map(int,input().split()))
# #print(nums)
# l = []
# sum = 0
# for i in range(len(nums)):  
#     sum += nums[i]
#     l.append(sum)
# print(l)


n = int(input("lenght of list "))
nums = list(map(int,input().split()))
#print(nums)
#l = []
sum = 0
for i in range(len(nums)):  
    sum += nums[i]
    #l.append(sum)
    print(sum,end = " ")
print()