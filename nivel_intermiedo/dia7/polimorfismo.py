# Explicación:

# El polimorfismo permite que distintos objetos respondan al mismo 
# método de forma distinta.

# Podés tener una lista de objetos diferentes, todos con un método 
# accion(), y aunque se llame igual, cada objeto actúa diferente.

# Ejercicio 2 – Practicar:

# Usando las clases del ejercicio anterior (Guitarra y Tambor), creá 
# una lista con ambos y hacé que toquen dentro de un for.

class Intrumentos():
    def tocar(self):
        pass

class Guitarra(Intrumentos):
    def tocar(self):
        return "stayk with meeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

class Tambor(Intrumentos):
    def tocar(self):
        return "pun chiqui"  

lista = [Guitarra(), Tambor()]

for instrumentos in lista:
    print(instrumentos.tocar())