#Python code to check the element existence using List count() method

test_list = [12, 22, 32, 42, 52]

exist_count = test_list.count(42)

if exist_count > 0:
    print("Element exist in the list")
else:
    print("Element not exist in the list")
