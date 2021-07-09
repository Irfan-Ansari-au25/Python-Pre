


num = "00001"
num = num[::-1]


dec = 0

for i in range(len(num)):
    digit = int(num[i]) * (2 ** i)
    dec += digit
print(dec)

