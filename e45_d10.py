import random

numero_random = random.randint (1, 11)
culea = int(input("Dime un numero: "))

if culea == numero_random:
    print("Bien echo! Lo ass encontrado")
else:
    print("Prueba otra vez")