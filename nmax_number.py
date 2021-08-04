# Python program to find N largest element from given list of integers

def maxnumber_n(list, n):
    final_list = []


    for i in range(0, n):
        max = 0
        for j in range(len(list)):
            if list[j] > max:
                max = list[j]

        list.remove(max)
        final_list.append(max)

    print(final_list)

list = [11, 2, 99, 22, 89]
n = 2
print(maxnumber_n(list, n))
