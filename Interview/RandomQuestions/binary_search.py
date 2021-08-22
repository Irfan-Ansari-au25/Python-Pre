

# for binary search array must be sorted
A = [1,7,23,44,53,63,67,72,87,91,99]

def binary_search(A,target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if target < A[mid]:
            high = mid - 1
        elif target > A[mid]:
            low = mid + 1
        else:
            return mid
        # print(low,high)
    return -1
    
print(binary_search(A,1))
