 #Python3 program to find remainder when all array elements are multiplied.

def find_reminder(arr, lens, n):
    mul = 1
    for i in arr:
        mul = mul * (i % n)
    return mul % n

arr = [2, 3, 4, 5]
n = 6
lens = len(arr)
print(find_reminder(arr, lens, n))
