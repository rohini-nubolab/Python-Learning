# Python program to find largest number in a list

list = [100, 0, 90, -1]

large = list[0]

for i in range(len(list)):

    if list[i] > large:
        large = list[i]

print("Largest number is:", large)
