# Python program to find smallest number in a list

list = [100, 0, 90, -1]

min = list[0]

for i in range(len(list)):

    if list[i] < min:
        min = list[i]

print("Smallest number is:", min)
