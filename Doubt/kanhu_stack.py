class MinStack():
    # Constructor, it initializes when object is created
    def __init__(self):
        self.stack = []

    def push(self,a):
        self.stack.append(a)
        return self.stack

    def pop(self):
        if len(self.stack) == 0:
            print( 'stack is empty, push element first :')
            return None
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        if len(self.stack) < 2:
            print("can't use built in fun(min) for less than two ele")
            return None
        return min(self.stack)

if __name__ == '__main__':
    stack = MinStack()
    print(stack.push(2))
    print(stack.push(-19))
    print(stack.pop())
    print(stack.top())
    print(stack.push(67))
    print(stack.get_min())
