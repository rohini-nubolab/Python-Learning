# Python3 code to demonstrate clearing a list using del method

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print("List before deleting:" + str(list1))

del list1[:]
print("List after deleting" + str(list1))


print("List before deleting:" + str(list2))

del list2[:]
print("List after deleting:" + str(list2))
