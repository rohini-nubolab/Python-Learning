# Python3 Program to find sum of square of first n natural numbers

def square_sum(n):
    
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
        
    return sm
    
n = 8
print("The sum of square of first", n, "number is", square_sum(n))
