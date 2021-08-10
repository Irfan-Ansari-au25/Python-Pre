"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
199
001
------------------------
200
"""

digits = [1,2,3,4,5,6,9,9,9]
digits = [0]

def plusOne(digits):
    carry = 0
    carry = (digits[-1] + 1 )// 10
    digits[-1] = (digits[-1] + 1) % 10

    i = len(digits) - 2
    
    while i > 0 :
        x = (digits[i] + carry ) % 10
        carry = (digits[i] + carry) // 10
        digits[i] = x
        i -= 1
    if carry > 0:
        digits.insert(0, carry)
    return digits

print(plusOne(digits))




