



sum = 100

def local_scope():

    for i in range(1,10):
        sum = 20
        print("Value of local variable", sum)

sum = 0
print("value of global variable", sum)

local_scope()
