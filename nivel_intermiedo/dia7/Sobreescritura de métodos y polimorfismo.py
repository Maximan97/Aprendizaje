# Concepto 1: Sobreescritura de métodos (override)
# Explicación:

# Cuando una clase hija tiene un método con el mismo nombre que uno en 
# la clase padre, lo que hace es sobrescribirlo.

# Esto permite que cada subclase personalice su comportamiento, aunque 
# todas tengan el mismo nombre de método.

# Ejercicio 1 – Practicar:

# Creá una clase Instrumento con un método tocar().
# Luego creá dos clases hijas: Guitarra y Tambor, cada una sobrescribiendo 
# tocar() con un mensaje diferente.

class Intrumentos():
    def tocar(self):
        print("Me re toco")


class Guitarra(Intrumentos):
    def tocar(self):
        print("stayk with meeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

class Tambor(Intrumentos):
    def tocar(self):
        print(f" pun chiqui" *3) #

patricio = Guitarra()
patricio.tocar()
patricio1 = Tambor()
patricio1.tocar()