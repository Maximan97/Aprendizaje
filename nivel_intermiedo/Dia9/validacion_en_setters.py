#  Explicación:

# Uno de los grandes usos del setter es validar lo que se está por guardar.
# Evita datos incorrectos o peligrosos.

#  Ejercicio 3 – Practicar:

# Creá una clase Jugador con un atributo nivel.
# Usá un setter que solo permita subir el nivel (nunca bajarlo).

class Jugador():
    def __init__(self, nivel):
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, nuevo_nivel):
        if nuevo_nivel > self._nivel:
            self._nivel = nuevo_nivel