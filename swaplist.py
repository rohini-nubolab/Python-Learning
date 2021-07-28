# Python3 program to swap first and last element of a list

def swaplist(newlist):
    
    size = len(newlist)
    
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp
    return newlist
    
newlist = [12, 15, 30, 56, 100]
print(swaplist(newlist))
