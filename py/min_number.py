#Max value from a list

numbers = []
lenght = int(input("Enter list lenght...\n"))
for i in range(lenght):
    numbers.append(float(input("Enter an integer or decimal number...\n")))

print("The min value is: " + str(min(numbers)))
    


