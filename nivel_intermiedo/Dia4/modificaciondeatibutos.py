# Creá una clase Jugador con un atributo puntos que empieza en 0. 
# Agregale un método anotar() que sume 10 puntos.
# Creá un jugador, hacé que anote 3 veces y mostrale los puntos finales.

class Jugador():
    def __init__(self):
        self.puntos = 0

    def anotar(self):
        self.puntos += 10

nahue = Jugador()

for i in range(100):
    nahue.anotar()

print(nahue.puntos)