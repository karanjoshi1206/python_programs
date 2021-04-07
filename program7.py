# By Karan joshi
# Program7: Create a function that take an integer and return its factorial

def factorial(num):
    fact = 1
    if(num < 0):
        print("Sorry factorial does not exists ")
    elif (num == 0):
        print("Factorial of 0 is 1 ")
    else:
        for i in range(1, num+1):
            fact = fact*i
        print("Factorial of the number is ", fact)


num = int(input("Enter the number whose factorial you waant to find "))
factorial(num)
