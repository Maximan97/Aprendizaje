# Dia 3 - Funciones Anidadas, Closures y Decoradores

# Concepto 1: Funciones anidadas

# Que es?
# Una funcion anidada es una funcion definida dentro de otra funcion. Se usan 
# para organizar mejor el codigo o para crear funciones que solo se usan en 
# un contexto especifico.

# Ejemplo:
# def saludar(nombre):
#   def mesaje():
#       return "hola"
#       return mensaje()+ "," + nombre
# print(saludar("Juan"))

# Ejercicio:
#  Crea una funcion que reciba un numero y defina adentro otra funcion que 
# sume 10 a ese numero.
# Retorna el resultado.

def numero(numero: int):
    def suma():
        return + 10
    return numero + suma()

print(numero(66))

# Concepto 2: Closures

# Que es?
# Un Closure es una funcion interna que "recuerda" los valores de las variables
# de su entorno incluso despues de que la funcion externa ha terminando de ejecutarse.

# Ejemplo:
#       del multiplicador(n):
#           del multiplicar(x):
#           return x * n
#       return multiplica
#
# doble = multiplicardor(2)
# print(doble(5))  # 10

# Ejercicio:
# Crea un Closure llamado crear_contador que reciba un numero inicial y devuelva una
# funcion que, cada vez que se llame sume 1 al numero y lo muestre.

def crear_contador(numero):
    def contador():
        return + 1
    return numero + contador()

suma = crear_contador(1)
print(suma)

# Concepto 3: Decoradores

# que es?

# Un decorador es una funcion que envuelve otra funcion para modificar o extender su 
# comportamiento sin cambiar su codigo original. Se usan con el simbolo @.

# Ejemplo:

#def mayusculas(func):
#    def wrapper():
#       resultado = func()
#       return resultado.upper()
#    return wrapper

#@mayusculas 
#def decir_algo():
#   return "hola mundo"

#print(decir_algo()) # HOLA MUNDO

# Ejercicio

# Crea un decorador llamado verificar_edad que permita ejecutar una funcion solo si 
# la edad es mayor o igual a 18. Si no, que imprima un mensaje de "Acceso denegado"

def menores(funcion):
    def wrapper(edad):
        if edad >= 18:
            print ("pasa")
        else:
            print("acceso denegado")
    return wrapper
    

@menores
def mayores(edad: int):
    return "Pasa, dale"

patas = mayores(17)
patas = mayores(18)
patas = mayores(19)