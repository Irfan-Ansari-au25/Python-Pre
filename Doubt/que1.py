

# doubt
# def count(strs):
#     cnt = 0
#     for c in strs:
     
#         if int(c) != 0:
#             cnt += 1
#     return cnt
# print(count('1000'))


# s = "abbaca"
# # Output: "ca"

# stack = list()

# for ch in s:
#     if ch not in stack:
#         stack.append(ch)
#     else:
#         stack.pop()

# ans = ''.join(stack)
# print(ans)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for el in s:
            if el == '(' or el == '{' or el == '[' :
                stack.append(el)   
            else:
                if len(stack) != 0:
                    if stack[-1] == '(' and (el == ')'):
                        stack.pop()
                        if len(stack) == 0:
                            return 'true'
                    elif stack[-1] == '{' and el == '}':
                        stack.pop()
                        if len(stack) == 0:
                            return 'true'
                    elif stack[-1] == '[' and el == ']':
                        stack.pop()
                        if len(stack) == 0:
                            return 'true'
                else:
                    if len(stack) != 0:
                        return 'false'
                    else:
                        return 'true'
        
                        
                
        # print(stack)
        # if len(stack) == 0:
        #     return 'true'
        # else:
        #     return 'false'

        
        
        
        """
              state = ''
            
        stack = list()
        
        while b in s == bracket:
            if b == bracket:
                stack.append(b)
            else:
                if len(stack) == 0:
                    state = 'false'
                    return state
                else:
                    stack.pop()
        if len(stack) == 0:
            state = 'true'
            return state
        
        return state
        
        def isValid(self, s: str) -> bool:

            paren = self.check_validation(s,'(')
            angle = self.check_validation(s,'{')
            square = self.check_validation(s,'[')
            print(paren,angle,square)

            # if (paren == 'true') and (angle == 'true') and (square == 'true'):
            #     return 'true'
            # else:
            #     return 'false'

        
        """
  
            
        
            
        

        
            
        
        
        