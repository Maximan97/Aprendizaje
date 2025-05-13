# Pedí al usuario una edad. Si la escribe mal, mostrá un error. Si 
# sale todo bien, imprimí un mensaje. Y siempre, al final, imprimí 
# “Gracias por usar el programa.”

try:
    edád = int(input("Dime tu edad: "))

except ValueError:
    print("ERROR")

else:
    print("Bien")

finally:
    print("Arigatou for use programu")