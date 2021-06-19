"""

*
**
***
****


"""


def print_stars_pattern(rows):
    for row in range(1,rows + 1):
        for stars in range(row):
            print("*", end="")
        print()

print("Please enter number of rows:", end="")
rows = int(input())

pattern = print_stars_pattern(rows)
print(pattern)