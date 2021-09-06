

# Given a string of parenthesis, s = '((()))())'


def is_valid(s):
    stack = list()
    for p in s:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    return False

if __name__ == '__main__':
    s = '((())())'
    print(is_valid(s))


