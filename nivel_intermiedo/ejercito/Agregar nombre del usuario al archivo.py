nombre = input("Tu nombre: ")
with open("C:/Users/jamji/maxi/nivel_intermiedo/ejercito/usuarios.txt", "a") as archivo:
    archivo.write(nombre + "\n")