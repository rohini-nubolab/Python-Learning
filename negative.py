# Python program to print Negative Numbers in a List

list = [1, 2, -1, 6, -7, 8, 10]

print("Given numbers are", list)
print("Negative numbers are")

for i in list:

    if i <= 0:
        print(i)
