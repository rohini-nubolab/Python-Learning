# Check if all items in the following tuple are the same
# tuple1 = (45, 45, 45, 45)

def check(sampleTuple):
		return all(i == sampleTuple[0] for i in sampleTuple)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))
