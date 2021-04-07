# By Karan joshi
# Program7: Create a function that take an single character input and return its char code of its lowercased / uppercased counterpart
def char_code_convert(character):
    lower_case_code = ord(character.lower())
    upper_case_code = ord(character.upper())
    return (lower_case_code, upper_case_code)


character = input("Enter the character ")
lower, upper = char_code_convert(character)
print("Char code of lowercase is ", lower, "and of uppercase is ", upper)
