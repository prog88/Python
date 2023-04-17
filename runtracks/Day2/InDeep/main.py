# declaration
def TriangleType(a, b, c):
    if a == b and b == c: 
        print("Equilateral triangle.")
    elif a == b or b == c or a == c:
        if (a*a+b*b==c*c) or (b*b+c*c==a*a) or (c*c+a*a==b*b):
            print("Right-angled Isoscles triangle.")
        else:
            print("Isosceles triangle.")
    elif (a*a+b*b==c*c) or (b*b+c*c==a*a) or (c*c+a*a==b*b):
        print("Right-angled triangle.")
    else:
        print("Any triangle.")


# execute
TriangleType(8,8,8)

TriangleType(6,6,8)
TriangleType(8,6,6)
TriangleType(6,8,6)

TriangleType(6,8,10)
TriangleType(6,10,8)
TriangleType(8,6,10)
TriangleType(8,10,6)
TriangleType(10,6,8)
TriangleType(10,8,6)

TriangleType(1,2,3)
TriangleType(2,3,1)
TriangleType(3,1,2)