"""
For type casting just wrap the value withints

>>int()
>>float()
>>str()

"""

print("Please enter your birth year")
birth_year = int(input())

age = 2021 - birth_year
print("Your age is :", age , "years old.")