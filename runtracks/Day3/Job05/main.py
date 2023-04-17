# definitions
def Is_Prime(n):
    for i in range(2,int(n/2)):
        if (n%i) == 0:
            return False
    return True

def Display_Prime_Number():
    for indice in range(1,1001):
        if Is_Prime(indice):
            print(indice)

# exec
Display_Prime_Number()