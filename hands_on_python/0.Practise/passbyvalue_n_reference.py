

def double(arg):
    print('Pass by value')
    print('before:', arg)
    arg = arg * 2
    print('after:', arg)

def change(arg):
    print('Pass by reference')
    print('before:', arg)
    arg.append('More data')
    print('after:', arg)

num =[1,2,5,6]
print(double(num))
print(num)
print(change(num))
print(num)
