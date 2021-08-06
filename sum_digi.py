# Python3 code to demonstrate Sum of number digits in List using loop + str()

list = [13, 45, 61, 79]

print("The original list is : " + str(list))

list1 = []
for ele in list:
    sum = 0
    for num in str(ele):
        sum = sum + int(num)
    list1.append(sum)

print("Sum of number digits are", str(list1))
