# Explicación:

# Ambas son formas de reutilizar código, pero tienen enfoques distintos:

    # Herencia: cuando decís "esto es un tipo de eso"

    # Composición: cuando decís "esto tiene un eso"

# Usar herencia para todo puede crear estructuras rígidas. La composición 
# da más flexibilidad.

# Ejercicio 3 – Practicar:

# Imaginá un sistema de videojuegos.
# Creá una clase Jugador y una clase Inventario.
# El jugador debe tener un inventario (no heredar de él).
# Agregá un método que muestre los ítems del inventario desde la 
# clase Jugador.

class Jugador():

    def __init__(self, inventario):
        self.invetario = inventario

    def muestrar_items(self):
        self.invetario.mostrar_inventario()


class Inventario():
    def mostrar_inventario(self):
        print("itemns")