# definition
def DisplayWithoutExceptions():
    exceptions = [26, 37, 88]
    for indice in range(0,101):
        if indice not in exceptions:
            print(indice)

# exec
DisplayWithoutExceptions()