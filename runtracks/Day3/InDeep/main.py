# define
def Reversed(inputString):
    buffer = ""
    for indice in range(len(inputString)):
        buffer += inputString[(len(inputString)-1)-indice]
    return buffer

# exec
source = "nikana"
print(Reversed(source))