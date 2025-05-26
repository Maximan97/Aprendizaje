from e46_2 import agregar_contacto, buscar_contacto

directonario = {"Maximiliano": "520516"}

while True:
    print("1. Agregar Contacto.")
    print("2. Buscar Contacto.")
    print("3. Mostrar Todo.")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_contacto(directonario)
    
    elif opcion == "2":
        buscar_contacto(directonario)

    elif opcion == "3":
        print(directonario)

    else:
        print("Saliendo")
        break