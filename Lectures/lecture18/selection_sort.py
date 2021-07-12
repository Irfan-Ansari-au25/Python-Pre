
A = [9, 3, 6, 1,7, 4, 2]


n = len(A)

for i in range(n):

    min_idx = i

    for j in range(i + 1, n):
        if A[j] < A[min_idx]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
print(A)