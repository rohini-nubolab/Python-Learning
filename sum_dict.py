# Python3 Program to find sum of all items in a Dictionary

def returnSum(myDict):
	
	sum = 0
	for i in myDict:
		sum = sum + myDict[i]
	
	return sum

dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict))

