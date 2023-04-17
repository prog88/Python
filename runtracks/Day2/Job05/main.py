# definition
def Compute(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2

# execute
print(Compute(6, "+", 2))
print(Compute(6, "-", 2))
print(Compute(6, "*", 2))
print(Compute(6, "/", 2))
print(Compute(6, "%", 2))
