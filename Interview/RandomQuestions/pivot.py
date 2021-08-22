A = [1,7,3,6,5,6,7,4]
# output 4
l = len(A)

print(l, A)

pivot = A[1:l-1]
# print(pivot,'pivot')

no_of_key = l-2

keys = [i for i in range(1,l-1)]
# print(keys,'keys')

def sol(keys):
    sum1 = 0
    for i in range(1,l):
        sum1 += A[i]
        if sum1 == 0:
            return 0
    sum2 = 0
    for i in range(l-1):
        sum2 += A[i]
        if sum2 == 0:
            return l-1
    for idx in keys:
        # print('idx',idx)
        lhs = 0
        rhs = 0
        for i in range(idx-1,-1,-1):
            lhs += A[i]
        for j in range(idx+1,l):
            rhs += A[j]
        # print(idx,lhs,rhs)
        if lhs == rhs:

            return idx
    
    return -1
print(sol(keys))
