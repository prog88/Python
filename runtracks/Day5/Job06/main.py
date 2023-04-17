# define
def Find_Next_Rounded_Value(mark):
    num = mark + 2
    num1 = mark + 1
    if num % 5 == 0 or num1 % 5 == 0:
        if num % 5 == 0:
            return "Succeed with score of: "+ str(num)
        elif num1 % 5 == 0:
            return "Succeed with score of: "+ str(num1)
        else:
            return "Succeed with score of: "+ str(mark)
    else:
        return "Succeed with score of: "+ str(mark)

def Succeed_Or_Failed(mark):
    if mark < 40:
        return "Failed"
    elif 40 <= mark and mark <= 100:
        return Find_Next_Rounded_Value(mark)
    else:
        return "Invalid mark"

# exec
print(Succeed_Or_Failed(39))
for index in range(40, 100):
    print(Succeed_Or_Failed(index))
print(Succeed_Or_Failed(101))