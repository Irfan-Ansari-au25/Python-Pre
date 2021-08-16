"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        #edge
        if len(s) % 2 != 0:
            return False
        #array
        a = list(s)
        print(a)
        print(len(s))
        
        #case 1
        sample = ['()', '{}', '[]']
        #case 2
        sample2 = ['(','{','[']
        
        # s = '(){}[](){}[]'
        l = len(s)
        print(len(s),'len of s')
        
        state = False
        for i in range(0,l+1,2):
            pair = (s[i:i+2])
            if pair in sample:
                state = True
            if pair not in sample:
                state = False
        if state == True:
            return True
        else:
            # s1 = list('[{()}]')
            s1 = list(s)
            half = len(s1)//2
            test = []
            i = 0
            while i < half:

            #     print(s1.pop(0))
                test.append(s1.pop(0))
                print(s1,'s1',len(s1))
                print('pop_add', test)
            #     test.insert(-1,s[half+i-1])
            #     print('rev_add', test)
                i += 1
            print(test,'final')
            print(s1, 's1 final')
            # test += s1
            # print(test,'ad')
            final = []
            for i in range(len(test)):
                final.append(test[i])
                final.append(s1[-1-i])

            final = ''.join(final)
            print(final,'s1')
            
            state1 = False
            for i in range(0,len(final)+1,2):
                pair = (final[i:i+2])
                if pair in sample:
                    print(sample,'sample')
                    print(pair,'pair',type(pair))
                    print(str(pair) in a)
                    print(state1, 'state1')
                    state1 = True
                if pair not in sample:
                    state1 = False
                    print('yes')
            if state1 == True:
                return True
            else:
                return False
                
        


        
            
            
        
            
        

        
            
        
        
        