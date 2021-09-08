class Solution:
    def isValid(self, string: str) -> bool:
        s = []
        for i in string:
            if i in "[{(":
                s.append(i)
            else:
                if len(s)>0:
                    tmp = s.pop(-1)
                    if tmp=="[" and i=="]":
                        continue
                    elif tmp=="(" and i==")":
                        continue
                    elif tmp=="{" and i=="}":
                        continue
                    else:
                        return False
                else:
                    return False
        if len(s)==0:
            return True
        else:
            return False
        

"""
preeti

class Solution:
    stack1=[]
    #stack={[)}
    
    def isEmpty(self):
        return len(self.stack1) == 0
    def peek(self):
        if self.isEmpty() :
            return None
        else :
            return self.stack1[-1]
    def push(self,x):
        self.stack1.append(x)
    def pop(self):
        self.stack1.pop()
            
    def isValid(self, s: str) -> bool:
        for i in s:
            if i == '(' :
                self.push(i)
            elif i == ')'and self.peek() =='(' :
                self.pop()
            elif i == '{' :
                self.push(i)
            elif i == '}'and self.peek() =='{' :
                self.pop()
            elif i == '[' :
                self.push(i)
            elif i == ']'and self.peek() =='[' :
                self.pop()
            else:
                print(False)
                break
        return self.isEmpty()


"""