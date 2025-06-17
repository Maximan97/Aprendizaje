# Concepto 2: Paquetes (__init__.py)

# ¿Qué es?

# Un paquete es una carpeta que contiene módulos, y que tiene un archivo 
# especial llamado __init__.py.
# Eso le dice a Python: “esto no es solo una carpeta, es un paquete 
# importable”.

# Ejercicio 2 – Practicar

# Creá una carpeta herramientas con un archivo __init__.py y un archivo 
# texto.py.

# En texto.py, hacé funciones para: contar letras, invertir texto, 
# capitalizar.

# Usalas desde otro archivo con from herramientas import texto.

# TIP: Si te da error, revisá que estés ejecutando el archivo desde el 
# lugar correcto (usualmente la raíz del proyecto).

from herramientas.text import palabra, palabra1, palabra2

print(palabra("paralelopipedo"))
print(palabra1("neuquen"))
print(palabra2("leTLelo"))