A =[1,2,4]
B= [3,5,7,8,9]
n = len(A)
m = len(B)
p1 = 0
p2 =0
C = []
while p1 < n or p2 < m:
    if p1 ==len(A):
        C.append(B[p2])
    else:

        if A[p1] < B[p2]:
            C.append(A[p1])
            p1 += 1
        else:
            C.append(A[p2])
            p2 += 1
print(C)

