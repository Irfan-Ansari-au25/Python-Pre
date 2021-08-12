"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
"""
x = -123
def reverse( x: int) -> int:
    
    if x == 0:
        return 0
    elif x > 0:
        l = []
        x = str(x)
        for i in x :
            l.append(i)

        l = l[::-1]
        l = ''.join(l)
        
        if  int(l) > (2**31 - 1):
            return 0
        else: 
            return int(l)
            
    else:
        x = str(x)
        l1 = []
        for i in range(1,len(x) ):
            l1.append(x[i])
        l1 = l1[::-1]
        l1 = ''.join(l1)
        
        if -int(l1)  < -(2**31):
            return 0
        else:
            return -int(l1)
print(reverse(x))