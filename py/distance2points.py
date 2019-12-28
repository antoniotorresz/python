
x1 = int(input("Enter x1 value bellow: "))
x2 = int(input("Enter x2 value bellow: "))

y1 = int(input("Enter y1 value bellow: "))
y2 = int(input("Enter y2 value bellow: "))


def computeDistance(x1, x2, y1, y2):
    #return math.sqrt((math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2)))
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Distance between points is: " + str(computeDistance(x1, x2, y1, y2)))