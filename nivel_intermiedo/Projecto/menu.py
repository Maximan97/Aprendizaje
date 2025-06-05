from definiciones import agregar_libro, prestar_libro, librero

print("Bienvenido a la Biblioteca.")
print("")
print("1. Agregar libro a alal.")
print("2. Pedir libro a la Biblioteca.")
print("3. Mostrar todos los libros disponibles.")
print("0. Salir")
print("")
opcion = input("Que opción eliges?: ")

while True:
    if opcion == "1":
        agregar_libro()

    elif opcion == "2":
        prestar_libro()

    elif opcion == "3":
        print(librero)

    elif opcion == "0":
        print("Nos vemos.")

    else:
        print("No es una opción valida.")
