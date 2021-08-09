"""
A = [1,2,3,4,9,8,12]

"""

# A = [1,2,3,4,9,8,12]
# B = []

# idx = 0
# for i in range(len(A) - 1): 
#     if A[i] > A[i + 1]:
#         idx = i - 1
#     else:
#         B.append(A[i])
# sec = A[idx:len(A)]
# print(sec)
# B = B + sec[::-1]
# sorted_array = B
# print(sorted_array)
# print('idx',idx, A[idx])
# def check_for_sorted_array(sorted_array):
#     for i in range(len(B) - 1): 
#         if sorted_array[i] > sorted_array[i + 1]:
#             return 'Not sorted when flipped'
    
#     return "sorted when flipped"
# print(check_for_sorted_array(sorted_array))
    
A = [1,2,3,9,7,5]
B = []
n = len(A)
idx = 0
def unsorted_array():
    for i in range(n - 1):
        # print(A[i], A[i +1])
        if A[i] > A[i + 1]:
            print(i,A[i], 'i values')
            return (A[i : n + 1])
        else:
            B.append(A[i])
sec = unsorted_array()

result = B + sec[::-1]
print(result)

def check_for_sorted():
    for i in range(n - 1):
        if result[i] > result[i + 1]:
            return "not sorted"
    return "sorted"
print(check_for_sorted())
