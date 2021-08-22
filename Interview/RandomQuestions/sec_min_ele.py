l = 7

A = [1, 8,2, 1,  2,3, 4]


def solution(A,l):
    if l <=3 or l >= 10000:
        return -1
    else:
        smallest = A[0]
        idx = 0
        for i in range(1,l):
            # print(A[i])
            if A[i] < smallest:
                smallest = A[i]
                idx = i

        # print(smallest,idx)
        B=[]
        for i in range(l):
            if A[i] > smallest:
                B.append(A[i])
        # print(A)
        # print(B)

        sec_small = B[0]
        for i in range(1,len(B)):
            if B[i] < sec_small:
                sec_small = B[i]
        print(sec_small,'sec')

        idx2 = []
        for i in range(l-1,-1,-1):
            # print(A[i])
            if A[i] == sec_small:
                idx2.append(i)
                
        return(idx2[0])
print(solution(A,l))