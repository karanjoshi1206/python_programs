# By Karan joshi
# Program9: Create a function that take list and finds the integer which appears an odd number of times.
def find_odd_count(lst):
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count = count+1

    if count % 2 != 0:
        return lst[i]
    return -1


# main code
lst = []
n = int(input('Enter the number of values '))
for i in range(0, n):
    value = int(input(' Enter the value '))
    lst.append(value)


print("The number which appears odd number of times is ", find_odd_count(lst))
