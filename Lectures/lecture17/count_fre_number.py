
array = [1,1,2,5,5,5,7,7,9,9,9,9,9,11]

def upper_bound(array, target):
    previous = -1
    for i in range(len(array)):
        # if array[i] == target:
        #     if array[i] > target:
        #         print("i")
        #         return f"hi {i}" 
        previous = i

        if array[i] > target:
            return previous 


def lower_bound(array, target):
    previous = -1
    for i in range(len(array)):
        if array[i] == target:
            return i 
        previous = i

        if target < array[i]:
            return previous - 1


def freq_count(array, target):
    ub = upper_bound(array, target)
    lb = lower_bound(array, target)
    print(lb)
    print(ub)
    if (ub - lb) == 1:
        return "Frequency is 1"
    else:
        return f"Frequency is {ub - lb }"

print(freq_count(array, 1))

## revisit this problem , something's wrong here


