"""
>>> todos = open('file_name', 'a') --a means append mode
>>> print('Put out the trash.', file = todos)
>>> print('Feed the cat.', file = todos)
>>> print('Prepare tax return.', file = todos)
>>> todos.close()
# to read the lines of a file
>>> any_var = open('file_name')
>>> for line in any_var:
        print(line)

----------------------------------------------------
A better open, process, close: 'With'
>>> with open('file_name) as any_var:
        for i in any_var:
            print(i, end='')

"""