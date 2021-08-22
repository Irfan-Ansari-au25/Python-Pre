

 #    0 1 2 3 4 5 
A = [7,3,8,9,2,11]
# find smallest number
#  exchange that number with A[1]
# continue for n-1 elements 

l = len(A) # 6

for i in range(l-1): # 0 1 2 3 5
    smallest = A[i]
    idx = 0
    for j in range(i,l):      # 0 1 2 3 4 5
        if A[j] <= smallest:
            smallest = A[j]
            idx = j
    key =  A[i]
    A[i] = smallest
    A[idx] = key
print(A)