# Python3 program to swap elements at given positions

def swapPosition(list, pos1, pos2):
    
    list[pos1], list[pos2] = list[pos2], list[pos1]
    
    return list
    
list = [10, 20, 30, 40, 50]
pos1, pos2 = 2,4
print(swapPosition(list, pos1-1, pos2-1))
