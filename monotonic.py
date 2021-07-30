# Python3 program to find sum in Nth group Check if given array is Monotonic.

def monotonic(A):
    
    return (all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


A = [6, 5, 4, 4]

print(monotonic(A))
