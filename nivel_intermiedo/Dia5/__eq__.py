# 🔎 Explicación:
#               Por defecto, dos objetos diferentes aunque tengan los 
# mismos datos no son iguales (== compara ubicación en memoria).
# Con __eq__, podés definir cuándo dos objetos deberían considerarse 
# iguales.

#  Ejercicio 3 – Practicar:
#                         Creá una clase Libro con título y autor.
#  Definí __eq__ para que dos libros sean iguales si tienen el mismo 
# título y el mismo autor.

class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __eq__(self, otro):
        return self.titulo == otro.titulo and self.autor == otro.autor
    
libro1 = Libro("Lumilagro", "Orlnia")
libro2 = Libro("Mate", "Orlnia")

print(libro1 == libro2) # Da "False"