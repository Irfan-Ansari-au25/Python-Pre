"""
Q-2 ) Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
(5 marks)
You are given two integer arrays nums1 and nums2, sorted in
non-decreasing order, and two integers m and n, representing the number
of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing
order.
The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length
of m + n, where the first m elements denote the elements that should be
merged, and the last n elements are set to 0 and should be ignored. nums2
has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of
the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.
"""



def merge(nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
     
        p1 = 0
        p2 = 0
        # print(nums1,nums2)
        while (p1<m) and (p2<n):
            
            if nums1[p1] <= nums2[p2]:
                nums1.append(nums1[p1])
                p1 += 1
                
            elif nums1[p1] > nums2[p2]:
                nums1.append(nums2[p2])
                p2 += 1
        
        while p1<m:
            nums1.append(nums1[p1])
            p1 += 1

        while p2<n:
            nums1.append(nums2[p2])
            p2 += 1
            
        for i in range(m+n):
            nums1.pop(0)
        
        print(nums1)
        
if __name__ == "__main__":

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    merge(nums1,m,nums2,n)