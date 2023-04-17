# Custom Implementation of Len()
def Count(list):
    count = 0
    for element in list:
        count += 1
    return count

# Sort and Merge
def Sort_Lists(leftList, rightList):
    resultList = []
    i = 0
    j = 0
    while i < Count(leftList) and j < Count(rightList):
        if leftList[i] <= rightList[j]:
            resultList.append(leftList[i])
            i += 1
            continue
        resultList.append(rightList[j])
        j += 1
    while i < Count(leftList):
        resultList.append(leftList[i])
        i = i+1
    while j < Count(rightList):
        resultList.append(rightList[j])
        j = j+1
    return resultList

# Main Sort
def My_Sort(list):
    if Count(list) <= 1:
        return list
    leftSubList = list[0 : Count(list) // 2]
    rightSubList = list[Count(list) // 2 : ]

    ansLeft = My_Sort(leftSubList)
    ansRight = My_Sort(rightSubList)

    sortedList = Sort_Lists(ansLeft, ansRight)
    return sortedList

# Remove Duplicated
def Get_Removed_Duplicated_From(list):
    resultList = []
    bufferedValue = list[0]
    resultList.append(bufferedValue)
    for element in list:
        if bufferedValue < element:
            bufferedValue = element
            resultList.append(bufferedValue)

    return resultList

# Apply Sort Before remove Duplicated
def Remove_Duplicated_From(list):
    if Count(list) < 1:
        return []
    sortedList = My_Sort(list)
    return Get_Removed_Duplicated_From(sortedList)

# Execution
inputList = [10,20,30,20,10,50,60,40,80,50,40]

print(Remove_Duplicated_From(inputList))