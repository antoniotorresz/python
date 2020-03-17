import numpy as np
#random.normal nos da valores decimales
#random.randint nos da valores enteros
def generateNumbers(n, max):
    random_matrix_array = np.random.randint(1,max,n)
    print(random_matrix_array)
    print("summatory: " + str(add(random_matrix_array)))
def add(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i]
    return sum
generateNumbers(int(input("Enter the quantity of numbers to generate...")),
 int(input("Enter the max value...")))