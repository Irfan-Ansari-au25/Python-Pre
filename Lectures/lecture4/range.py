"""
Loops
for and while
Range

"""

# print(list(range(2,10, 1)))

for i in range(1,31, 1):
    if (i%3 == 0 and i%5 == 0):
        print("FIZZ_BUZZ")
    elif (i%3 == 0):
        print("FIZZ")
    elif (i%5 == 0):
        print("FUZZ")
    
    else:
        print(i)
    
# Not printing a new line after print command
print("hello")
print("hi")
print("hello", end ="")
print("hi", end ="&&")