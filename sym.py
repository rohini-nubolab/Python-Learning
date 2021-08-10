# Function to check whether the
# string is symmetrical or not

def symmetric(string):

    n = len(string)
    flag = 0

    if n%2:
       mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid
    while(start1 < mid and start2 < n):
        if(string[start1] == string[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 0
            break

    if flag == 0:
       print("Given string is symmetrical")

    else:
        print("Given string is not symmetrical")
string = "khokho"
symmetric(string)
