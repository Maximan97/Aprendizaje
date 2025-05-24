# Explicación:

# La composición es cuando una clase contiene instancias de otras clases.
# En lugar de decir “un Estudiante es un Usuario”, decimos “un Estudiante 
# tiene un Usuario”.

# Es una forma de construir relaciones sin herencia.

# Ejercicio 1 – Practicar:

# Creá una clase Pantalla con un método mostrar().
# Luego creá una clase Celular que contenga una instancia de Pantalla y 
# tenga un método encender_pantalla() que llame al método de Pantalla.

class Pantalla():  
    def mostrar(self):
        print("Me encendi -.-?")

class Celular():
    def __init__(self):  
        self.pantalla = Pantalla()  # ESTO ES IGUAL A LO DE ARRIBA
# OSEA, POR ASI DECIRLO, CLONA Y USA LA CLASE PANTALLA 

    def encender_pantalla(self):
        self.pantalla.mostrar()   # MAS DE LO MISMO