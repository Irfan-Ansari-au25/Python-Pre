
result = []
def plusOne( digits):
    
    str1 = "".join(str(i) for i in digits)
    print (str1)
    num1 = int(str1) + 1
    print(num1)
    num2 = str(num1)
    
    for i in num2:
        result.append(int(i))
    return(result)
        
digits =[9,9,9]
print(plusOne(digits))