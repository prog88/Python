#define
def Count(list):
    count = 0
    for element in list:
        count += 1
    return count

def Get_Space_Position(stringSrc, stringSize):
    spacingIndexes = []
    for index in range(0, stringSize):
        if stringSrc[index] == " ":
            spacingIndexes.append(index)
    spacingIndexes.append(Count(stringSrc))
    return spacingIndexes

def Extract_Word_That_Match(startPosition, endPosition, stringSrc):
    characterBuffer = []
    stringResult = ""
    for index in range(startPosition+1, endPosition):
        characterBuffer.append(stringSrc[index])

    for char in characterBuffer:
        stringResult += char
    return stringResult

def My_Long_Word(length, inputString):
    result = ""
    spacingArray = Get_Space_Position(inputString, Count(inputString))
    for index in range(0, Count(spacingArray)-1 ):
        num1 = spacingArray[index]
        num2 = spacingArray[index+1]
        if num2 - num1 > length + 1:
            result += Extract_Word_That_Match(num1, num2, inputString)
            result += " "
    return result

# exec
source = " La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"

print(My_Long_Word(3, source))