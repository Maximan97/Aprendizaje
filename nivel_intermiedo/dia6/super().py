# 🔎 Explicación:

# Cuando una clase hija quiere tener su propio __init__, pero también usar 
# el del padre, se usa super().

# Esto evita repetir código del padre.

# 🧪 Ejercicio 3 – Practicar:

# Modificá Perro para que, además del nombre heredado, tenga un atributo raza.
# Usá super() para inicializar el nombre.

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza