# Dia 2 - Programacion Funcional    

# Concepto 1: Funciones Lambda

# ¿Que es?

# Una Lambda es una forma rapida de crear funciones pequeñas sin necesidad de usar def.
# Ideal para funciones que se usan una sola vez.

# Ejercicio 1 

# Usa Lambda para crear una funcion que reciba un numero y devuelva el doble.
# Luego, otra que devuelva el numero al cuadrado.

sumar = lambda a: a+a
print(sumar(10))

multiplicar = lambda a: a*a
print(multiplicar(5))

# Concepto 2: map()

# ¿Que es?

# map() aplica una funcion a cada elemento de una lista( u otra coleccion).
# Devuelve un objeto que podes convertir en lista con list().

# Ejercicio 2 

# Tenes esta lista:
# nombres = ["ana", "bruno", "CARLA", "dAvid"]
# Usa map() para poner todos los nombres con la primera letra en mayuscula y el resto en minuscula.

nombres = ["ana", "bruno", "CARLA", "dAvid"]

correccion = list(map(lambda nombre:  nombre.capitalize(), nombres))
print(correccion)

# Concepto 3: filter() y reduce()

# filter() 
# #filtra elementos que cumplen una condicion.
 
# numero = [1, 2, 3, 4, 5, 6]
# pares = list(filter(lambda x: x%2 == 0, numeros))
# print(pares) #[2, 4, 6] resultado

# reduce() 
# Usa una funcion que acumula valores, uno por uno.
# Necesitas importar reduce desde functools.

# fron functools import reduce
# nummeros = [1, 2, 3, 4]
# suma = reduce(lambda a, b: a+b, numeros)
# print(suma) #10

# Ejercicio 3

# Lista de edades.

# edades = [14, 22, 19, 30, 17, 40]

# Con filter(), quedate solo con los mayores de edad

# Con reduce(), suma todas las edades

edades = [14, 22, 19, 30, 17, 40]
mayores = list(filter(lambda edad: edad >= 18, edades))
print(mayores)

from functools import reduce

suma = reduce(lambda a, b: a + b , edades)
print(suma)