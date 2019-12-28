#This program will allow you to find a straight that ajusts to the following data through least squares method
#Using matplotlib
#Graph libraries
from matplotlib import pyplot as plt
from matplotlib import lines as line

xList = [7, 1, 10, 5, 4, 3, 13, 10, 2]
yList = [2, 9, 2, 5, 7, 11, 2, 5, 14]



def getList_summatory(x):
    sumatory = 0
    for i in range(len(x)):
        sumatory += x[i]

    return sumatory

def getXY_summatory(x, y):
    xy_sum = 0
    if not len(x) > len(y) or len(y) > len(x):
        for i in range(len(x)):
            xy_sum += (x[i] * y[i])
    return xy_sum


def getXPow_summatory(x):
    xpow_sum = 0
    for i in range(len(x)):
        xpow_sum += x[i] **2
    return xpow_sum


def getA_value():
    x_sum = getList_summatory(xList)
    xpow_sum = getXPow_summatory(xList)
    y_sum = getList_summatory(yList)
    xy_sum = getXY_summatory(xList, yList)

    a = ((len(xList) * xy_sum) - (x_sum * y_sum)) / ((len(xList) * xpow_sum) - x_sum **2)
    print("A value is: "+ str(a))
    return a

def getB_value():
    y_sum = getList_summatory(yList)
    x_sum = getList_summatory(xList)
    
    b = (y_sum - (getA_value() * x_sum)) / len(xList)
    print("B value is: " + str(b))
    return b

print("Y value is: " + str(getA_value() + getB_value()))

def getPoints():
    points = []
    for i in range(len(xList)):
        points.append([xList[i], yList[i]])
    
    print(points)
    return points


a = getPoints()
plt.plot(*zip(*a),  marker='o', color='b', ls='')
plt.plot([0, (getA_value() + getB_value())], [-1 * (getB_value() / getA_value()), 0], color = "r")
plt.title("y = mx + b")
plt.show()