directorio = {"Maximiliano": "620516",
            "Leonel": "654123",
            "Naue": "987456"}

def agregar_contacto(diccionario):
    namae = input("Dame un nombre: ")
    number = input("Dame el numero: ")
    diccionario[namae] = number # agrega nombre y numero 
    print(diccionario)
    print("Ya fue agregado.")

def buscar_contacto(diccionario):
    busca = input("Buscamos: ")
    if busca in diccionario:
        print(diccionario[busca])

    else:
        print("No Esta")


while True:
    print("1. Agregar contacto.")
    print("2. Buscamos contacto.")
    print("3. Ver todo.")
    print("4. Salir.")
    
    opcion = input("Que hacemo' vieja: ")

    if opcion == "1":
        agregar_contacto(diccionario=directorio)
    
    elif opcion == "2":
        buscar_contacto(diccionario=directorio)

    elif opcion == "3":
        print(directorio)
    
    elif opcion == "4":
        print("saliendo' gato")
        break

    else:
        print("Que hace gato")