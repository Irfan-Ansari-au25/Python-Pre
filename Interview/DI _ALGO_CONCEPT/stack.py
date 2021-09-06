"""
It's a list when it's follow stacks convention it becomes a stack.

"""


stack = list()
#stack = bottom[8,5,6,3,9]top

def isEmpty():
    return len(stack) == 0

def peek():
    if isEmpty():
        return None
    return stack[-1]

def push(x):
    return stack.append(x)

def pop():
    if isEmpty():
        return None
    else:
        return stack.pop()

if __name__ == '__main__':
    push(8)
    push(5)
    push(6)
    push(3)
    push(9)
    print(isEmpty())
    print(peek())
    x = pop()
    print(x,'pop')
    print(stack)