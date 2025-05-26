# Explicación:

# Con @property podés hacer que parezca que accedés a un atributo, pero en realidad estás llamando un método.
# Esto permite controlar la lectura y escritura.

# Ejercicio 2 – Practicar:

# Creá una clase Temperatura con un atributo _celsius.
# Usá @property para poder leerlo y cambiarlo, pero solo si es un número 
# válido

class Temperatura():
    def __init__(self, celcius):
        self._celcius = celcius

    @property  #akxede a la linea 12
    def celcius(self):
        return self._celcius

    @celcius.setter #akzede y cambia el parametro que le demos a Temperatura()
    def celcius(self, nuevo):
        if nuevo != "":
            self._celcius = nuevo 
        else:
            print("MAMAHUEVO, DIGO GLU GLU GLU")