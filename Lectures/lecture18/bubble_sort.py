
A = [6,3,9,7,4,76,34,23,11]

for i in range(len(A) - 1) :
    print(i, "loop i")
    

    for j in range(0, len(A) - i - 1):
        print(j, "loop j")
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
        

print(A)    