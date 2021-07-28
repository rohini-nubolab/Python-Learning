# Python3 code to clear a list using reinitializing method

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print("List before clearig:" + str(list1))

del list1[:]
print("List after clearig" + str(list1))


print("List before using reinitializing:" + str(list2))

list2 = []
print("List after reinitializing:" + str(list2))
