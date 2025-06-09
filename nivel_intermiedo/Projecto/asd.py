# Proyecto Final – Simulador de Biblioteca Digital
# 🧠 Objetivo:

# Crear un pequeño sistema para gestionar una biblioteca digital.
# Se deben poder agregar libros, ver información, prestar libros, y
# controlar accesos y errores.

# 🧱 Requisitos (¡Sí o sí!):

# 1. ✅ Usar Clases
#     Debe haber al menos 2 clases principales: Libro y Biblioteca.
#     Usá herencia si te parece útil (por ejemplo, si hacés una
#     clase ItemBiblioteca como base).

# 2. ✅ Encapsulamiento
#     Algunos atributos deben estar marcados como privados o protegidos
#     (_atributo, __atributo).
#     Accedé a ellos usando @property y @setter con validación.
#     Ejemplo de atributo privado sugerido: __disponible, __prestado_a,
#     _cantidad_disponible.

# 3. ✅ Validaciones y manejo de errores
#     Si alguien intenta prestar un libro que no existe → mostrar mensaje.
#     Si alguien pone un dato incorrecto (por ejemplo, una cantidad
#     negativa) → manejarlo con try/except o validaciones.
#     TIP: Usá isinstance(valor, int) para chequear tipos, y raise
#     ValueError("mensaje") para lanzar errores propios.

# 4. ✅ Composición (opcional pero recomendado)
#     Que Biblioteca contenga una lista de objetos Libro.
#     Es decir, un libro no vive solo, vive dentro de la biblioteca.

# 5. ✅ Funciones que simulen acciones
#     agregar_libro(): agrega un nuevo libro
#     prestar_libro(nombre): marca el libro como prestado si está
#     disponible.
#     mostrar_libros_disponibles(): lista todos los que se pueden prestar.
#     # TIP: Podés usar listas y bucles para recorrer los libros.

estanteria = []


class Libro():
    def agregar_libro(self):
        n_libro = input("dime el nombre del libro: ")
        estanteria.append(n_libro)
        print(f"{n_libro} fue agregado en la biblioteca.")
        print("Muchas gracias.")

    def buscar_libro(self,):
        b_libro = input("el libro que buscamos es: ")
        if b_libro in estanteria:
            print(f"{b_libro} fue encontrado.")
        else:
            print("No esta.")

    def prestar_libro(self, libro):
        self.libro = libro
        if buscar_libro():
            b_libro = libro
            estanteria.remove(libro)
            print("Que lo disfrutes.")
        else:
            print("No esta")


class Biblioteca(Libro):
    def __init__(self):
        while True:
            print("1. Agregar libro a la biblioteca.")
            print("2. Pedir un libro a la biblioteca.")
            print("3. Mostrar los libros en la biblioteca.")
            print("o. Salir.")
            print("Bienvenido a la biblioteca.")
            opcion = input("Elige una opción.")

            if opcion == "1":
                agregar_libro()

            elif opcion == "2":
                buscar_libro()

            elif opcion == "3":
                print(estanteria)

            elif opcion == "0":
                print("Nos vemos. Tenga usted un buen dia")

            else:
                print("Opción no valida. Prueba con las opciones que te damos.")
