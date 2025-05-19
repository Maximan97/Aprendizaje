# 🔎 Explicación:
#               Este método permite definir lo que significa "longitud" 
# para tus objetos.
# Se usa cuando hacés len(objeto).
# Por ejemplo, en una clase Libro, podrías usar __len__ para que devuelva 
# la cantidad de páginas.

# Ejercicio 2 – Practicar:
#                        Creá una clase Playlist que tenga una lista de
# canciones.
# Definí el método __len__ para que devuelva cuántas canciones hay.

class Playlis():
    def __init__(self):
        self.playlist = ["mia", "orl", "net", "dis", "you", "pri"]

    def __len__(self):
        return len (self.playlist)
    
lista = Playlis() 
print(len(lista)) # Da "6"