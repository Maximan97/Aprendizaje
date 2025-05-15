# Agregá al Libro un __init__ que reciba titulo y autor. Luego creá 
# un objeto con un título y autor inventados y mostralos en pantalla.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

libero = Libro("Reino fungi", "Bass")
print(libero.titulo, libero.autor)