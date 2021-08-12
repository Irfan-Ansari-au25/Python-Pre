"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
"""

def isPalindrome( x: int) -> bool:
    rev = ''.join(list(reversed(str(x))))
    print(rev)
    
    return str(x) == rev

x = -123
print(isPalindrome(x))
    