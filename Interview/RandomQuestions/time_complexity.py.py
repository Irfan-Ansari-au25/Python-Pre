


n = 5
count = 0
for i in range(n):
    j = 1
    
    while(j<=i**2 and n > 0):
        n -= 1
        for k in range(n//2):
           count+=1
           print('Time complexity',count)

    