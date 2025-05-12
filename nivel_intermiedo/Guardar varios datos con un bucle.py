with open("usuarios2.txt", "a") as archibo:
    for i in range(3):
        nombre = input("Dame tu nombre, lo guardare bien: ")
        edad = input("Dame tu edad: ")
        archibo.write(f"Nombre: {nombre} Edad: {edad}  \n")