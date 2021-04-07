# By Karan joshi
# Program5: Create a function that take list containing only numbers and return the first element

def lst_func(lst):
    return lst[0]


lst = []
n = int(input("Enter the number of elements "))
for i in range(0, n):
    elements = int(input())
    lst.append(elements)
print(lst_func(lst))
