# define
L = [8, 24, 48, 2, 16]

def Count_Elements_Which_Is_Mutiple_of_Three(list):
    counter = 0
    for value in list:
        if value % 3 == 0:
            counter+=1
    return counter

# exec
print(Count_Elements_Which_Is_Mutiple_of_Three(L))