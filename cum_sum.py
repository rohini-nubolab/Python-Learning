# Python code to get the Cumulative sum of a list

list = [2, 4, 6, 7]

list1 = []
j = 0
for i in range(0, len(list)):
    j = j + list[i]
    list1.append(j)

print(list1)

