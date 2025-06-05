librero = []


def agregar_libro():
    libro = input("Nombre del libro?: ")
    librero.append(libro)
    print(f"{libro} ya fue agregado al librero.")


def buscar_libro(libro):
    if libro in librero:
        return True
    else:
        return False


def prestar_libro():
    libro = input("Que libro te queres llevar?: ")
    if buscar_libro(libro):
        librero.remove(libro)
        print("Ya lo tienes en el inventario")
    else:
        print("Te lo ganaron wey")
