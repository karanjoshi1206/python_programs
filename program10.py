# By Karan joshi
# Program7: Create a function name "Reverser" which take string as an input and return the string in reversed orde,with opposite case
def Reverser(str):

    swapped_case = str.swapcase()
    rev_string = swapped_case[::-1]
    return(rev_string)


string = input("Enter the string to reversed  ")
print("Reversed string with changed cases is :", Reverser(string))
