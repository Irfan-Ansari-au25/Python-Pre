class Solution:
    def trap(self, height) -> int:
        max_left = 0
        mid = 1
        max_right = 2
        trap = 0
        
        while height[max_left] >=height[max_right]:
            max_right += 1
            continue
        area_min = min(height[max_left],height[max_right])
        print(area_min)
        a = max_right-(max_left+1) 
        print(a,'a')
        b = (height[(max_left+1)],height[(max_right)])
        print(b,'b')
        total =height[(max_left+1):max_right]
        leng = len(total)
        print(total,'total',leng)
        t = (area_min*leng) - sum(total) 
        print(t,'t')
        return t
        
        max_left = max_right
        max_right = max_left + 1
        print(max_left,'max_left',max_right,'max_right')
            
        
sol = Solution()
height = [4,2,0,3,2,5]
#         0 1 2 3 4 5 6 7 8
# sol.trap([2,1,0,1,3,2,1,2,1])
sol.trap(height)