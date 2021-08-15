"""
 Roman to Integer
Easy

1462

111

Add to List

Share
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        
        for i in range(len(s)):
            if s[i] == 'I':
                result += 1
                if i+1 < len(s):
                    if s[i+1] == 'V' :
                        result -= 2
                    elif s[i+1] == 'X':                                                                                                                                                                                                                                             
                        result -= 2
            elif s[i] == 'V':
                result += 5
            ######################
            elif s[i] == 'X':
                result += 10
                if i+1 < len(s):
                    if s[i+1] == 'L' :
                        result -=20
                    elif s[i+1] == 'C':
                        result -= 20
            elif s[i] == 'L':
                result += 50
            ###################
            elif s[i] == 'C':
                result += 100
                if i+1 < len(s):
                    if s[i+1] == 'D' :
                        result -=200
                    elif s[i+1] == 'M':
                        result -= 200
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
            
        return result

sol = Solution()
print(sol.romanToInt("MCMXCVIII"))
                