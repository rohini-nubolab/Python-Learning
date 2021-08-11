# Python3 code to demonstrate working of Convert Snake case to Pascal case
# Using title() + replace()

string = "Python_programming_language"

print("Given string is :" + string)

result = string.replace("_", " ").title().replace(" ", " ")

print("String after changing case : " + str(result))
