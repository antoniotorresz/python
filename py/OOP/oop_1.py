class Car():
    chasisLength = 250
    wheels = 4
    power = False


#self makes reference to the instance in class
#self hace referencia a una instancia al objeto de la misma clase
#self equivale a this en otros lenguajes
    def turnOn(self):
        self.power = True
    def changeLenght(self, n):
        self.changeLenght = n

car1 = Car()
print(car1.power)
print(car1.chasisLength)
car1.turnOn()
car1.changeLenght(1200)
print(car1.power)
print(car1.chasisLength)
