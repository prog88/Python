# define
L = [1, 2, 3, 4, 5]

def ReplaceValueAt(position):
    if 0 < position and position < len(L)-1:
       L[position] = L[position-1] + L[position+1]

# execute
print(L[1])
ReplaceValueAt(3) # replace L[3] by L[2]+L[4]
print(L[len(L)-1])