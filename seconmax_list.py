# Python program to find second largest number in a list

list = [11,12,13,14]

mx = max(list[0], list[1])
second_max = min(list[0], list[1])
n = len(list)

for i in range(2, n):
    if list[i] > mx:
        second_max = mx
        mx = list[i]

    elif list[i] > second_max and mx != list[i]:
        second_max = list[i]

print("Second highest number is : ", str(second_max))
