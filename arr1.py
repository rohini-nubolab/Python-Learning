def sum(arr):
    
    sum = 0
    for i in arr:
        sum = sum + i
    return sum
    
arr = []

arr = [12, 3, 4, 15]
n = len(arr)
a = sum(arr)
print("Sum of array is", a)
