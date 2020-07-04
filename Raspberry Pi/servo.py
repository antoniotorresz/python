# Importamos las librerias
import RPi.GPIO as GPIO
import time

# Agregamos el modo del pin GPIO
GPIO.setmode(GPIO.BOARD)

# Le decimos que el pin 11 sera salida y se define la variable servo1 como pin PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# Hacemos que empieze a correr PWM, con el valor de 0 
servo1.start(0)

# Bucle para prpeguntar el angulo a girar del servo

try:
    while True:
        angle = float(input('Ingresa un angulo entre 0 y 180 grados: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    #Liberamos memoria de los GPIO
    servo1.stop()
    GPIO.cleanup()
    print("Adiós!")
