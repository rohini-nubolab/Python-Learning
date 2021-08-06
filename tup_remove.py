# Python2 program to remove empty tuples from a list of tuples function to remove empty tuples using filter

def remove_tup(tuples):
    tuples = filter(None, tuples)
    return tuples


tuples = [(), ('Ram', 2, 4), ('Ravi','Sita'), ()]
print(remove_tup(tuples))
