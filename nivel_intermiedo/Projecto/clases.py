class Libro():
    def __init__(self, titulo):
        self._titulo = titulo

    @property
    def titulo(self):
        return self._titulo


class Mostrador():
    def menu(self):
        print("")
        print("Bienvenido a la Biblioteca.")
        print("")
        print("1. Agregar libro a alal.")
        print("2. Pedir libro a la Biblioteca.")
        print("3. Mostrar todos los libros disponibles.")
        print("0. Salir")
        print("")
        self.opcion = input("Que opción eliges?: ")
        return self.opcion


class Biblioteca():
    def __init__(self):
        self.librero = []
        mostrador = Mostrador()
        while True:
            self.opcion = mostrador.menu()
            if self.opcion == "1":
                self.agregar_libro()
            elif self.opcion == "2":
                self.prestar_libro()
            elif self.opcion == "3":
                for libro in self.librero:
                    print(libro.titulo)
            elif self.opcion == "0":
                print("Nos vemos.")
                break
            else:
                print("No es una opción valida.")

    def agregar_libro(self):
        titulo = input("Nombre del titulo?: ")
        libro = Libro(titulo)
        self.librero.append(libro)
        print(f"{titulo} ya fue agregado al librero.")

    def buscar_libro(self):
        if self.titulo in self.librero:
            return True
        else:
            return False

    def prestar_libro(self):
        self.titulo = input("Que titulo te queres llevar?: ")
        if self.buscar_libro():
            self.librero.remove(self.titulo)
            print("Ya lo tienes en el inventario")
        else:
            print("Te lo ganaron wey")


pito = Biblioteca()
