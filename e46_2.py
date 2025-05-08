def agregar_contacto(directonario):
    nombre = input("Dame el nombre: ")
    numero = input("Dame el número: ")
    directonario [nombre] = numero
    print(directonario)
    print("Ya esta agregado")
    
def buscar_contacto(directonario):
    buscar = input("A quien buscamos: ")
    
    if buscar in directonario:
        print(directonario[buscar])
    else:
        print("No esta.")
