"""
To convert into binary:
>>> bin(num)              
To convert into octal:
>>> oct(num
To covert into hexadecimal:
>>> hex(num)
----------------------------------------------------
To replace somethin in a string:
>>> string.replace('old','new')    -> ref: help(str)
left/right/center justification:
>>> ljust(width,fillchar=')
Return a left justify string of length width,padding
is done using the specified fill char(def=space)

Syntax :
>>> ljust( WIDTH, fillchr )

Parameters :
********************* WIDTH : The width of string to expand it.********************
fillchr (optional): The character to fill in remaining space.
"""

# hands ON

# b = bin(12)             # 'ob1100'
# print(b,type(b))
# c = b.replace('0b','') # 1100
# print(c,'rep')
# d = c.center(4,'#')
# print(d,'justify')
# print(len(d),'len')







def sol(number):
    def dec_to_other(number, i):
        s = ''
        # hexa decimal
        hexa = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while number > 0:
            rem = number % i
            if i==16 and rem in hexa.keys():
                s += hexa[rem]
            else:
                s += str(rem)
            number = number // i
        s = s[::-1]
        # print(s,'s')
        return s

    # calculating width
    width = len(dec_to_other(99,2))
    # print(width,'22')


    for i in range(1, number+1):
        hexadec = dec_to_other(i,16).rjust(width)
        decimal = str(i).rjust(width)    
        octal = dec_to_other(i,8).rjust(width)
        binary = dec_to_other(i,2).rjust(width)
        print(f'{decimal} {octal} {hexadec} {binary}')
sol(17)
        