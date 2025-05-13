# Pedí al usuario que ingrese un número. Si escribe algo incorrecto 
# (por ejemplo: "hola"), mostrá un mensaje que diga que el valor no
# es válido.

try:
    n = int(input("Dime números guarros: "))

except ValueError:
    print("Valor no valido.")