def buscar_nombre(lista, nombre):
    if nombre in lista:
        return True
    else:
        return False
        
print(buscar_nombre(["Naue", "Gera", "David", "Gonza"], "leo"))