# Python program to remove empty list from a list

list = [11, [], 33, [], 9, 12]

print("Given List", list)
list1 = [num for num in list if num != []]
print("List after removing empty list : " + str(list1))
