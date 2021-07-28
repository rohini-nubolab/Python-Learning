# Python program to find sum of elements in list
total = 0
ele = 0

list = [11, 21, 31, 41]
while (ele < len(list)):
    total = total + list[ele]
    ele = ele + 1

print("Sum of elements is:", total)
