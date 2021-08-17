"""
Insertion sort is good for small number of elements.

Insertion-Sort(A):
A = [5,2,4,6,1,3]
for j 2 to A.length
    key = A[j]
    #insert A[j] into the sorted sequence[1...,j-1]

    i = j-1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key

"""
A = [5,2,4,6,1,3]

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

print(insertion_sort(A),'insertion_sort(ascending)')
    

"""
Three properties of
Loop Invariant:-(why algorithm is correct)
1. Initialization: It is true prior to the first iteration of the loop.
2. Maintenance: If it is true before an iteration of the loop, it remains true before the next iteration.
3. When the loop terminates, the Invariant gives us a useful property that helps show the algorithm is correct.


"""
A = [31,41,59,26,41,58]

def insertion_sort_decreasing(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1

        while i > -1 and A[i] < key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A
print(insertion_sort_decreasing(A),'insertion_sort')


"""
Binary sum

"""


def add_decimal(A, B):
    C = list(range(len(A)+1))
    
    carry = 0
    for i  in range(len(A)-1,-1,-1):
        
        C[i+1] = (A[i] + B[i] + carry) % 10 # remainder
     
        carry = (A[i] + B[i] + carry) // 10# quotient

    C[i] = carry
    return C

A = [1,2,3,4,5,6,7,8,9,7]
B = [9,8,7,6,5,4,3,2,1,5]

print(add_decimal(A,B),'adding two n size list')

