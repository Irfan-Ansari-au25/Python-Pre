"""

*
**
***
****


"""
#######################


def print_stars_pattern(rows):
    for row in range(1,rows + 1):
        for stars in range(row):
            print("*", end="")
        print()

print("Please enter number of rows:", end="")
rows = int(input())

pattern = print_stars_pattern(rows)
print(pattern)


###########################

# for i in range(1,5):
#     print("*" * i)


#########################

# count = 1
# while(count < 5):
#     stars = 0
#     while( stars < count):
#         print("*", end="")
#         stars += 1
#     print()
#     count += 1

