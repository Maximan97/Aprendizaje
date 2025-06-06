librero = ["pito"]


class Biblioteca():
    # Tiene estantes
    pass


class Libro():
    def __init__(self, titulo, estado):
        self.estado = estado
        self.titulo = titulo
    # Titulo
    # Estado

    def agregar_libro(self):
        libro = input("Nombre del libro?: ")
        librero.append(libro)
        print(f"{libro} ya fue agregado al librero.")

    def buscar_libro(self):
        if libro in librero:
            return True
        else:
            return False

    def prestar_libro(self):
        libro = input("Que libro te queres llevar?: ")
        if buscar_libro(self, libro):
            librero.remove(libro)
            print("Ya lo tienes en el inventario")
        else:
            print("Te lo ganaron wey")


class Estante(Libro):
    # Tiene libros
    librero = []

    def __init__(self):
        pass
