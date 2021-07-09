

def decimal_to_binary(no):
    num =""

  
    
    while no > 0:
        digit = no % 2
        num += str(digit)
        print(digit, num)
        
        no //= 2
        
    return(num[::-1])
    

x = decimal_to_binary(7)
print(x)
