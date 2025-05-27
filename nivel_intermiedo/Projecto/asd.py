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


class Libro(): # puede haber una herencia / # valor: int
    def __init__(self, nombre: str, titulo: str) -> None:
        self._nombre =  nombre # debe tener _privado
        self._titulo = titulo

    @property
    def nombre(self):
        return self._nombre
    @property
    def titulo(self):
        return self._titulo

    @nombre.setter
    def nombre(self, nuevo):
        if nuevo != "":
            self._nombre = nuevo
    @titulo.setter
    def titulo(self, nuevo):
        if nuevo != "":
            self._titulo = nuevo

class Biblioteca(Libro):
    def __init__(self, agregar_libro, prestado_libro, mostrar_libros):
        self.agregar_libro = agregar_libro 
        self.prestado_libro = prestado_libro
        self.mostrar_libros = mostrar_libros


operador = ["culo", "teta"]

mostrar_libros = operador

def agregar_libro(operador):
    nombre = input("Nombre del libro? ") # X
    titulo = input("Y su titulo es? ")
    operador[nombre] = titulo # ~ -> operador.append(titulo)
    print(operador)
    print("Ya fue agregado.")

def buscar_libro(operador):
    buscar = input("Nombre del libro?")
    if buscar in operador:
        print(operador[buscar])
        opsion = Input("Te lo llevas? [Y/N]")
    elif opsion == "Y":
        operador del buscar, titulo

    else:
        print("No esta disponible.")

while True:
    print("Bienvenido a la biblioteca")
    print("")
    print("1. Agregar libro.")
    print("2. Pedir libro.")
    print("3. Mostrar todos los libros.")
    print("0. Salir.")

    opcion = input("Elige una opción: ")

    if opcion == "1":
            agregar_libro(operador)

    elif opcion == "2":
        prestar_libro(operador)

    elif opcion == "3":
        print(operador)

    elif opcion == "0":
        print("Saliendo.")

    else:
        print("Opinion no valido.")