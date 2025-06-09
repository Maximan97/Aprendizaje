class Mostrador():
    def menu(self) -> str:
        """Muestra menú y retorna la opción elegida x usuario"""
        print("Bienvenido a la Biblioteca.")
        print("")
        print("1. Agregar libro a alal.")
        print("2. Pedir libro a la Biblioteca.")
        print("3. Mostrar todos los libros disponibles.")
        print("0. Salir")
        print("")
        opcion = input("Que opción eliges?: ")
        return opcion


class Estante():
    """Tiene libros"""

    def __init__(self):
        self.librero = ["pito"]


class Biblioteca():
    def __init__(self):
        self.mostrador = Mostrador()
        self.estante = Estante()
        self.librero = self.estante.librero

    def mostrar_menu(self):  # Muestra menú y pide opciones
        while True:
            opcion = self.mostrador.menu()
            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.prestar_libro()
            elif opcion == "3":
                print(self.librero)
            elif opcion == "0":
                print("Nos vemos.")
                break
            else:
                print("No es una opción valida.")

    def agregar_libro(self):
        titulo = input("Nombre del libro?: ")
        self.librero.append(titulo)
        print(f"{titulo} ya fue agregado al librero.")

    def buscar_libro(self, titulo):
        if titulo in self.librero:
            return True
        else:
            return False

    def prestar_libro(self):
        titulo = input("Que libro te querés llevar?: ")
        if self.buscar_libro(titulo):
            self.librero.remove(titulo)
            print("Ya lo tienes en el inventario")
        else:
            print("Te lo ganaron wey")
