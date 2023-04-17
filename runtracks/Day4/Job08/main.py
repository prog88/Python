# define
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def SumOfEvenValuesInList(values):
    sum = 0
    for value in values:
        if value % 2 == 0:
            sum+=value
    return sum

# exec
print(SumOfEvenValuesInList(L))