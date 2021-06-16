"""
if
elif
elif
else

is a controlled statement , statement breaks if one of them is true.

"""

x = 100
y = 200

if (x + y == 300):
    if (x < y):
        print("x is less than y")
    elif (y < x):
        print("x i greater than y")
    elif (x == y):
        print("x is equal to y")
    
    else:
        print("Error")

    if (x % 2 == 0):
        print("It's divisible by 2")
else:
    print("please enter another number")
    