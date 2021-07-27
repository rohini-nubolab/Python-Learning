#Python3 program to find maximum in arr[] of size n 

def large_arr(arr, n):
    
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
           max = arr[i]
    return max

arr = [10, 20, 90, 100, 30]
n = len(arr)
ans = large_arr(arr, n)
print("Largest number is ", ans)
