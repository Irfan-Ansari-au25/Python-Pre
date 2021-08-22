
"""
# A = [
#         ['#', '#', '#'],
#         ['#', '', '#'],
#         ['#', '#', '#'],
# ]


for 3 X 3 gap = 1         idx =[ (1,)]
for 4 X 4 gap = 2**2      idx = [(1,1),(1,2),(2,1),(2,2)]
for 5 X 5 gap = 3**3      idx = [((1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3))]
"""
ip= int(input('Enter row or column of a square matrix greater than 3 : '))
A = [[0 for i in range(ip)] for j in range(ip)]
# print(A)
rows = len(A)
cols = len(A[0])
list_of_non_border_ele = []

def findIdxOfGap(rows,cols):
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            # print(row,col)
            list_of_non_border_ele.append((row,col))


findIdxOfGap(rows,cols)

# print(list_of_non_border_ele)

def printBorderElements(rows,cols):
    for row in range(rows):
        for col in range(cols):
            if (row,col) in list_of_non_border_ele:
                A[row][col] = ' '
                print(A[row][col], end=' ')
            else:
                A[row][col] = '#'
                print(A[row][col], end=' ')
        print()
printBorderElements(rows,cols)
# print(A)
