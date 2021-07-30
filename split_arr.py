# Python program to split array and move first part to end.

def arr_split(arr, n, k):

    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
        arr[n - 1] = x


arr = [10, 12, 7, 8, 9]
n = len(arr)
position = 2

arr_split(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')
