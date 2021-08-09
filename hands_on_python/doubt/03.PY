"""
Q-2) Write a program to print sum of n natural numbers .
Eg n = 5 (5 marks)
Output 1 + 2 + 3 + 4 + 5 = 15

"""
n = 5
total = 0

for i in range(1, n + 1): #  1 2 3 4 5
    total += i
    print("for loop ",i, "total =", total)

print( "result", total)

