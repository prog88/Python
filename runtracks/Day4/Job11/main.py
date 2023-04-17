# define List comprehension
def generateValues(list):
    return [value+1 for value in list]

# exec
L = [7, 11, 42, 39, 2]
print(generateValues(L))