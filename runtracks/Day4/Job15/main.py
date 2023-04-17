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

# Sort and Round list 
def Get_Floor_Rounded(list):
    nbElement = Count(list)
    floorValue = 0
    listElementcounter = 0
    roundedList = []
    while nbElement > 0:
        if  floorValue <= list[listElementcounter] and list[listElementcounter] < floorValue + 1:
            roundedList.append(floorValue)
            listElementcounter += 1
            nbElement -= 1
        floorValue += 1
    return roundedList

# Handle only positive values
def Sorted_Rounded(list):
    if Count(list) < 1:
        return []
    sortedList = My_Sort(list)
    return Get_Floor_Rounded(sortedList)


# execute
inputValues = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(Sorted_Rounded(inputValues))