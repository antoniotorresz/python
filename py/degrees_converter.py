degrees = float(input("Enter °C degrees...\n"))

option = int(input("Choose an option:\n1.Convert to Fahrenheit\n2.Convert to Kelvin\n3.Both\n"))


def convert_farenheit(celsuis):
    return str((9/5 * celsuis) + 32)
def convert_kelvin(celsuis):
    return str(float(celsuis + 273.15))

result = ""

if option == 1:
    result = convert_farenheit(degrees) + "°F"
if option == 2:
    result = convert_kelvin(degrees) + "°K"
if option == 3:
    result = convert_farenheit(degrees) + " °F and " + convert_kelvin(degrees) + " °K"

print(str(degrees) + "°C equals to: " + result)