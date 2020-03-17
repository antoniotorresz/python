import numpy as np
#This program will give you the absolute value of a 2D array
#from its main diagonal summatories
def diagonalDifference(arr):
    try:
        first_sum = 0
        sec_sum = 0
        counter = len(arr[0]) -1
        for i in range(len(arr[0])):
            first_sum += arr[i][i]
        for j in range(counter + 1):
            sec_sum += arr[j][counter]
            counter -=1
        if not first_sum - sec_sum <= 0:
            return str(first_sum + sec_sum)
        else:
            return str(-1 * (first_sum - sec_sum))
    except:
        print("An error ocurred, try again.")
        main()

def main():
    try:
        array = np.random.randint(1, int(input("Enter the max value...")), size = (3,3))
        print(str(array) + " --> " + "|" + diagonalDifference(array) +"|")
    except:
        print("An error ocurred, try again...")
        main()

main()