class Solution: 
    
    def recursion(self,s):
        maxx = 0
        l = []
        if len(s) == 0:
            l.append(0)
            return '0' 
        
        d = {}                       # empty hash
        c = 0                        # count
        max_c = 0                    # maximum count
        
        for i in range(len(s)):
            if s[i] in d:
                d = {}
                c = 1
                d[s[i]] = i
                
            else:
                
                d[s[i]] = i
                c+=1
                print(d)
        
            if c > max_c:
                max_c = c
                print(max_c)
                l.append(max_c)
         # recursion
        if max(l)> maxx:
            maxx = max(l)
        
    
        self.recursion(s[1:len(s)])
        print('l',l,max(l),maxx)

        return maxx

        
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == len(set(s)):
            return len(s)
            
        else:
            
            ans = self.recursion(s)
            # ans = [int(ans[i]) for i in range(len(ans))]
            print(ans,'ans')
            # print('maxax',max(l))
            # return ans


s = "alqebriavxoo"