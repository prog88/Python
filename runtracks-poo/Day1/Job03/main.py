class Operation:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        print(self.number1 + self.number2)

operation = Operation(1,2)
operation.addition()