"""
n X m => rows & columns
diagonal in square matrix (0,0), (1,1), (2,2)
anti diagonal matrix 

matA = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
]

*** ***** ********************************python


>>> [0 for _ in range (3)]
>>> [0, 0, 0]

>>> [[0 for _ in range (3) ] for _ in range(3) ] 
>>> [
        [0,0,0],
        [0,0,0],
        [0,0,0]
]

*******  *** *************************

n = len(matA)
m = len(matA[0])

"""


matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)

mat = [
        [1,5,3],
        [4,8,6],
        [7,9,13]
]

print(mat)

n = len(mat)
m = len(mat[0])

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print()

for i in range(n):
    print(mat[i][i])

for i in range(n):
    for j in range(m):
        if( i + j == n-1):
            print(mat[i][j])
