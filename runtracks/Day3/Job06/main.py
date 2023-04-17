import string

# define
alphabetTimesTen = string.ascii_lowercase * 10

def printAlphaTree(buffer): 
    indice = 1
    while indice < len(buffer):
        print(buffer[:indice])
        buffer=buffer[indice:]
        indice+=1

# execute
printAlphaTree(alphabetTimesTen)