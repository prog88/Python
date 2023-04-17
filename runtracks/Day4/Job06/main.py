# define
L = [1, 2, 3, 4, 5]

def SwapFirstLast():
    if len(L) > 0:  # control not empty
        L[0], L[len(L)-1] = L[len(L)-1], L[0]

# execute
SwapFirstLast()
print(L)