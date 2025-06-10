class Libro():
    def __init__(self, titulo: str):
        self.titulo = titulo


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
        self.librero: list[Libro] = []
        mostrador = Mostrador()
        while True:
            self.opcion = mostrador.menu()
            if self.opcion == "1":
                self.agregar_libro()
            elif self.opcion == "2":
                self.prestar_libro()
            elif self.opcion == "3":
                if len(self.librero) != 0:
                    for libro in self.librero:
                        print(libro.titulo)
                else:
                    print("es de chisito")
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

    def prestar_libro(self):
        titulo = input("¿Qué libro querés llevarte?: ")
        for libro in self.librero:
            if libro.titulo == titulo:
                self.librero.remove(libro)
                print(f"Llevate '{titulo}', pero devolvelo, eh.")
                return
        print("Te lo afanaron, no está ese libro.")


pito = Biblioteca()
