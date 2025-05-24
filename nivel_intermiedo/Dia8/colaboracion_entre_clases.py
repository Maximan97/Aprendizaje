# Explicación:

# La colaboración se da cuando objetos de diferentes clases 
# trabajan juntos.
# En vez de tenerlo todo en una clase gigante, se dividen 
# responsabilidades y se llaman entre sí.

# Esto hace el código más modular y fácil de mantener.

#  Ejercicio 2 – Practicar:

# Creá una clase Reloj que tenga un método hora_actual().
# Luego creá una clase Persona que tenga un reloj como atributo y 
# un método decir_hora() que use el método del Reloj.

class Reloj():
    def hora_actual(self):
        print("no se la hora actual")

class Persona():
    def __init__(self, reloj): 
        self.reloj = reloj

    def decir_hora(self):
        self.reloj.hora_actual()


maxi_el_persona = Persona(Reloj()) 
# Instancia de la clase Persona con un atributo, que es la 
# clase Reloj() (Linea 21)