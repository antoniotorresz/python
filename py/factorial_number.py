#Recursive function to calculate factorial froma given number
def get_factorial(number):
    if not number == 0 or number == 1:
        return (get_factorial(number - 1) * number)
    else:
        return 1

x = int(input("Please, type a number to calculate its factorial: "))
print(str(x) + "! = " + str(get_factorial(x)))
