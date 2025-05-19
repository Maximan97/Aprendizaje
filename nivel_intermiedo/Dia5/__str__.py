# 🔎 Explicación:
#               Cuando imprimís un objeto, Python por defecto muestra 
# algo como <__main__.MiClase object at 0x0000...>.
#  Para cambiar eso, se puede definir un método especial llamado 
# __str__, que devuelve una cadena para mostrar el objeto con claridad.

# Practicar:
#           Creá una clase Pelicula con título y año.
# Agregale un método __str__ para que al imprimirla se vea así:
#                                                         Título (Año)

class Pelicula():
    def __init__(self, titulo, año: int):
        self.titulo = titulo
        self.año = año 

    def __str__(self):
        return f"{self.titulo} , ({self.año})"
    
pelicula = Pelicula("Minecraft", 2025)
print(pelicula)