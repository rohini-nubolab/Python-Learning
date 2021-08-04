# Python program to print positive Numbers in given range

start = 5
end = 15
print("Given Range Is", start,"-", end)
print("Positive Numbers from given range is")

for i in range(start, end+1):
    if i >= 0:
        print(i)
