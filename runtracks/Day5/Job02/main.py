# Draw in terminal

# define
def Draw_Box(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if j == 0 or j == width-1:
                print("|", end="")
            elif i == 0 or i == height-1:
                print("-", end="")
            else:
                print(" ", end="")
        print()

# exec
Draw_Box(10,3)