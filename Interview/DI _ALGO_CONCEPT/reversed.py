"""
reversed() Parameters
The reversed() function takes a single parameter:

seq - the sequence to be reversed
A sequence is an object that supports sequence protocols: __len__() and __getitem__() methods. For example, tuple, string, list, range, etc.

We can also use reversed() in any object that implements __reverse__().

"""
x = 'abc'
print(''.join(list(reversed(x))))