# Function to remove all duplicates from string and order does not matter

def rem_duplicate(str):

    s = set(str)
    s = "".join(s)
    print("Given string is : ", str)
    t = ""
    for i in str:
        if (i in t):
            pass
        else:
            t = t + i
    print("After removing duplicates: ", t, '\n')

str = "One by One"
rem_duplicate(str)

str = "geeks for geek"
rem_duplicate(str)
