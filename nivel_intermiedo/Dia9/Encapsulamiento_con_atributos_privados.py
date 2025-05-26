# Explicación:

# El encapsulamiento consiste en proteger los datos internos de una clase.
# En Python, no hay verdaderos "privados", pero por convención usamos 
# _atributo o __atributo.

# _atributo: indica que no debería tocarse desde afuera.

# __atributo: lo oculta internamente (name mangling).

# 🧪 Ejercicio 1 – Practicar:

# Creá una clase Cofre que tenga un atributo secreto __tesoro.
# Agregá un método mostrar_tesoro() para ver su valor.

class Cofre():
    def __init__(self, atributo_secreto):
        self.__tesoro = atributo_secreto

    def mostrar_tesoro(self):
        return self.__tesoro