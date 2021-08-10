"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twoSum(nums: 'List[int]', target: int) -> 'List[int]':
    result = list()
    n = len(nums)
    for i in range(n):
        for j in range(i):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return sorted(result)

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))