# Python code to count number of matching characters in a pair of strings

def count(str1, str2):

    a, b = 0, 0
    for i in str1:
        if (str2.find(i) >= 0 and b == str1.find(i)):
            a = a + 1
        b = b + 1

    print("Number of matching charecters are : ", a)

def main():
    str1 = 'python@123'
    str2 = '123.program'
    count(str1, str2)

if __name__=="__main__":
    main()
