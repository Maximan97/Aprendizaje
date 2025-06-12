import os


def borrar_pantalla():
    os.system("cls")  # Borra pantalla


def pausa():
    input("Presiona enter...")


class Libro():
    def __init__(self, titulo: str):
        self._titulo = titulo

    @property
    def titulo(self):
        return self._titulo


class Mostrador():
    def menu(self):
        borrar_pantalla()
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
                    pausa()
                else:
                    borrar_pantalla()
                    print("No hay libros agregados aun.")
                    pausa()
            elif self.opcion == "0":
                print("Nos vemos.")
                break
            else:
                borrar_pantalla()
                print("No es una opción valida.")
                pausa()

    def agregar_libro(self):
        titulo = input("Nombre del titulo?: ")
        if titulo == "":
            borrar_pantalla()
            print("No tiene nombre el libro.")
            pausa()
            return
        # if que se fije si está bacio si no, que de error (en else nene)
        #   # Esto inmpide que siga nbajando
        libro = Libro(titulo)
        self.librero.append(libro)
        borrar_pantalla()
        print(f"{titulo} ya fue agregado al librero.")
        pausa()

    def prestar_libro(self):
        borrar_pantalla()
        titulo = input("¿Qué libro querés llevarte?: ")
        if titulo == "":
            borrar_pantalla()
            print("No hay libros agregados a un?")
            pausa()
            return
        for libro in self.librero:
            if libro.titulo == titulo:
                self.librero.remove(libro)
                borrar_pantalla()
                print(f"Llevate '{titulo}', pero devolvelo, eh.")
                pausa()
                return
        borrar_pantalla()
        print("Te lo afanaron, no está ese libro.")
        pausa()


pito = Biblioteca()
