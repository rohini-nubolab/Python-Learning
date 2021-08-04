# Python program to print positive Numbers in a List

list = [1, 2, -1, 6, -7, 8, 10]

print("Given numbers are", list)
print("Positive numbers are")

for i in list:

    if i >= 0:
        print(i)
