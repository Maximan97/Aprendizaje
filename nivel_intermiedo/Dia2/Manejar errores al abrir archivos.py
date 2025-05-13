# Cuando intentás abrir un archivo que no existe, Python lanza un 
# error (FileNotFoundError). Con try y except, podemos detectar ese 
# problema y reaccionar, por ejemplo mostrando un mensaje en vez de 
# que el programa se rompa.

try:
    with open("Minecraft_trucho.txt", 'r') as Minecraft_Real:
        pass

except FileNotFoundError:
    print("Que estas buscando?")