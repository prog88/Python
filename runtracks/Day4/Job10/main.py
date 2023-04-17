# define
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def TimesValuesWithin(values):
    min = 25
    max = 90
    result = 1
    for value in values:
        if min <= value and value <= max: 
            result *= value
    return result

# exec
print(TimesValuesWithin(L))