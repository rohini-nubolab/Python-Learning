# Python program to generate and print 
# dictionary of numbers and square (i, i*i)

n = 10
numbers = {}

for i in range(1, n+1):
    numbers[i] = i * i
    
print(numbers)
