# Python program to find all string which are greater than given length k

def length_k(k, str):

    string = []
    text = str.split(" ")

    for i in text:

        if len(i) > k:
            string.append(i)
    return string

k = 4
str = "Python is a programming"
print(length_k(k, str))
