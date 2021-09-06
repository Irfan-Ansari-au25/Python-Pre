
def value(rom_sy):
    if (rom_sy == 'I'):
        return 1
    if (rom_sy == 'V'):
        return 5
    if (rom_sy == 'X'):
        return 10
    if (rom_sy == 'L'):
        return 50
    if (rom_sy == 'C'):
        return 100
    if (rom_sy == 'D'):
        return 500
    if (rom_sy == 'M'):
        return 1000
    return -1
 
 
def roman_to_Decimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            s2 = value(str[i + 1])
 
            if (s1 >= s2):
 
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res
 
print(roman_to_Decimal("MCMXCIV"))