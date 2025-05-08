def agregar_nombre(lista):   # creaaaa la lista
    nombres = input("Dime nombre: ")  # pido algo
    lista.append(nombres.lower())  # lista.append para agregar antes del nombre
    print(lista)  #  imprime la lista creada junto con el nombre
    
agregar_nombre(["Maxi", "Gera"])  # La mamos a la funcion