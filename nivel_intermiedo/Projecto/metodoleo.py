def main():
    while True:
        print("Bienvenido a la biblioteca")
        print("")
        print("1. Agregar libro.")
        print("2. Pedir prestado el libro.")
        print("3. Mostrar todos los libros.")
        print("0. Salir.")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            name = input("Dime el nombre del libro: ")
            agregar_libro(name)

        elif opcion == "2":
            name = input("Dime el nombre del libro: ")
            prestar_libro(name)

        elif opcion == "3":
            print(librerro)

        elif opcion == "0":
            print("Saliendo.")
            exit()

        else:
            print("Opinion no valido.")

librerro = ["lili"]

def agregar_libro(name):
    librerro.append(name)
    print(librerro)

def buscar_libro(name):
    for libro in librerro:
        if name == libro:
            return True
        else:
            return False

def prestar_libro(libro):
    if buscar_libro (name=libro):
        librerro.remove(libro)
        print("está")
    else:
        print("no ta")

class Libro():
    def __init__(self, titulo):
        pass

class Biblioteca(Libro):
    def __init__(self, libros: list[Libro]) -> None:
        pass

if __name__ == "__main__":
    main()