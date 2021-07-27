#Python program to find sum of series with cubes of first n natural numbers

def cube_sum(n):
    
    sm = 0
    for i in range(1, n+1):
    
        sm = sm + (i*i*i)
    return sm
    
n = 6
print(cube_sum(n))
