# definition
def DisplayFizzBuzz():
    for indice in range(1,101):
        if indice % 3 ==0 and indice % 5 == 0:
            print("FizzBuzz")
        elif indice % 3 == 0:
            print("Fizz")
        elif indice % 5 == 0:
            print("Buzz")
        else:
            print(indice)

# exec
DisplayFizzBuzz()