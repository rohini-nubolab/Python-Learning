# Python program to multiply all values in the list

def list_mul(list):

    mul = 1
    for i in list:
        mul = mul * i
    return mul

list1 = [2,3,4]

print(list_mul(list1))
