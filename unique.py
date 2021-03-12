# function to check unique


def check_unique(x):
    return len(x) == len(set(x))
    
x = [10, 20, 30, 40,50]

print("x: ", x)
print("len(x): ", len(x))
print("len(set(x)): ", len(set(x)))
print("check_unique(x): ", check_unique(x))
print()
