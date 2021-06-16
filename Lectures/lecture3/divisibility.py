# If a number is divisible by 4

num = int(input())

if (num%3 == 0 and num%5 ==0):
    print("FIZZ_BUZZ")
else:
    if(num%3 ==0):
        print("FIZZ")
    if(num%5 ==0):
        print("FUZZ")



