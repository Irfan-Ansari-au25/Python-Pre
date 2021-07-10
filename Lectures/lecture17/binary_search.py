"""
1.Linear search: time complexity is O(n), best O(1)
2.Binary search is applicable for only sorted list
    worst time complexity is O(log(n)), best O(1)

"""

array = [1,4,5,6,8,9,10,14,45,64,554]

def binary_search(array, target):
    right = len(array) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1

print(binary_search(array, 9))

