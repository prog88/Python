# define
def Draw_Slashed_Box(size):
    for i in range(0, size):
        for j in range(0, size): 
            if i == 0 or i == size-1:
                if j == 0 or j == size-1:
                    print("+", end="")
                else:
                    print("-", end="")
            elif j == 0 or j == size-1:
                print("|", end="")
            elif i == (size-1) - j:
                print(" ", end="")
            else:
                print("#", end="")
        print("")

# exec
size = 10
Draw_Slashed_Box(size)
