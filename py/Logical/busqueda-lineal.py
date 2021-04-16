from random import randint #(a, b)

lista = [randint(0, 100) for x in range(0, 10)]
print("Lista de numeros generados -> {}".format(lista))

encontrado = False
elemento = int(input('Ingrese un numero para buscarlo...'))

for e in lista: 
    if elemento == e:
        encontrado = True
        break

print("El numero {} está dentro de la lista? {}".format(elemento, encontrado))