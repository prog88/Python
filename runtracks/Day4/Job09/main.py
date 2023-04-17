# define
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def MinMaxInList(values):
    min = values[0]
    max = values[0]
    for value in values:
        if value <= min :
            min = value
        if value >= max :
            max = value
    return(min,max)

# exec
print(MinMaxInList(L))
print(min(L), max(L))