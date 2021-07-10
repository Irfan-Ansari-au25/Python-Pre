"""
lower bound: index of no less than the target or smallest index for same nos
upper bound: index of no greater than the target or greater index for same nos

>>> [1,2,2,2,5,5,6,7,8,8,8,9]

lb(2) = idx:1
lb(3) = idx:3

"""
array = [1,2,2,2,5,5,6,7,8,8,8,9]

def lower_bound(array, target):
    index = -1
    for i in range(len(array)):
        if target == array[i]:
            return i
        if array[i] > target:
            return index
        
        index = i
print(lower_bound(array, 3))
