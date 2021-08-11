# Python code to demonstrate string length using for loop

def findLen(str):

    counter = 0
    for i in str:
        counter = counter + 1
    return counter

str = "Python"
print("Length of string is ", findLen(str))
