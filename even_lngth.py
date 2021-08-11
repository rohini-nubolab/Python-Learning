# Python3 program to print even length words in a string

def even_len(s):

    s = s.split(' ')
    for word in s:
        if len(word)%2 == 0:
            print(word)

s = "Python Learn"
even_len(s)
