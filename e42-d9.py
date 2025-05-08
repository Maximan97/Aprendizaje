# Crear una función que pida un nombre y devuelva su teléfono (si está en el diccionario).

def buscar_alguien(diccionario):
    busca = input("Buscamos: ")
    if busca in diccionario:
        print(diccionario[busca])

    else:
        print("No Esta")

buscar_alguien({"Maximiliano": 620516,
            "Leonel": 654123,
            "Naue": 987456})