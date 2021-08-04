# Python program to remove even numbers from a list

list = [11, 20, 33, 17, 9, 12]

print("Given List", list)

for num in list:
    
    if (num % 2 == 0):
        list.remove(num)
print("Numbers after removing even numbers from list", list)
