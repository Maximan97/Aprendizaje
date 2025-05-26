
# ejemplo con while ingresar número par
resultado = 1 # creamos variable para que funcione en while

while resultado != 0: # Mientras el resto de la div no sea 0
    numero = int(input("Por favor, ingrese un número: "))

    # formula para obtener par 
    # numero / 2 - (PE de numero / 2) == 0
    resultado = (numero / 2)
    resultado = resultado - (numero // 2)
