# Python code to clone or copy a list

def clone_list(list1):
    list2_copy = list(list1)
    return list2_copy


list1 = [11, 22, 33, 44, 55]
list2 = clone_list(list1)
print("Original list is ", list1)
print("Cloned list is", list2)
