def agregar_contacto(piccionario):
    namae = input("Dame un nombre: ")
    number = input("Dame el numero: ")
    piccionario[namae] = number # agrega nombre y numero 
    print(piccionario) # inprime el nuevo contracto


contacto = {"Maximiliano": "620516",
            "Leonel": "654123",
            "Naue": "987456"}

agregar_contacto(contacto)





#contacto["Leonel"] = "1238312758723" #- > aasigno
#print(contacto["Maximiliano"]) # -> muestrp