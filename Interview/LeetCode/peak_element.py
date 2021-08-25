"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

# Time complexity for this solution is O(n) , S(0):  O(1)
class Solution:
    def findPeakElement(self, nums: 'List[int]') -> 'int':
        l = len(nums)

        if l == 1:
            return 0
        
        j = 0
        
        if  nums[j]>nums[j+1]:
            return 0
        
        elif nums[l-1]>nums[l-2]:
            return l-1
        
        else:
            for i in range(l):
                if i>0 and nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                    return i

nums = [1,2,3,1]
sol = Solution()
print(sol.findPeakElement(nums))



