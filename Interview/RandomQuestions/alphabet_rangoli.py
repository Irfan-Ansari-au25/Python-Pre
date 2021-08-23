"""

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
l = (2*size-1)
w = 2l-1 
#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
n = 5 
length = (2*n-1)
width = (2*length-1)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
l = len(alphabet)
print(l)

def print_upper(n):

    for i in range(n-1,0,-1): #[0,1,2,3,4] 
        alpha =  alphabet[0+i:n][::-1] + alphabet[1+i:n]
        # print(alpha)
        lis = list(alpha)
        for i in range(1,len(lis)):
            lis.insert(2*i-1,'-')
        alpha = ''.join(lis).center(width,'-')
        print(alpha)
print_upper(n)
    

def print_lower(n): # 5
    for i in range(n): #[0,1,2,3,4] 
        alpha =  alphabet[0+i:n][::-1] + alphabet[1+i:n]
        # print(alpha)
        lis = list(alpha)
        for i in range(1,len(lis)):
            lis.insert(2*i-1,'-')
        alpha = ''.join(lis).center(width,'-')
        print(alpha)
print_lower(n)











# alpha = alphabet[1:n][::-1] + alphabet[:n]
# # print(alpha)
# lis = list(alpha)
# print(lis)
# for i in range(1,len(lis)):
#     lis.insert(2*i-1,'-')
# print(lis)
# alpha = ''.join(lis).center(width,'-')

# print(alpha)
    
# def print_lower(n):
#     alpha = alphabet[1:n][::-1] + alphabet[:n]
#     lis = list(alpha)
#     for i in range(n-1,0,-1):
#         # print(alpha)
#         if lis[(len(lis)//2)] == 'a':
#             lis.pop(len(lis)//2)
#         if 'a' not in lis:
#             lis.pop(len(lis)//2)
#             lis.pop(len(lis)//2)
    
#         print(lis,'lis')
#         for i in range(1,len(lis)):
#             lis.insert(2*i-1,'-')
#         print(lis)
#         alpha = ''.join(lis).center(width,'-')
#         print(alpha)
    
# print_lower(n)



