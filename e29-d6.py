contador = 0
clave = 0
resultado = 0

while True: # mientras q contador no llegue a Dios
    intentos = int(input("ingresa el numero clave: "))

    if clave != intentos:
        contador += 1
        print(contador)
        resultado += intentos
    else:
        print(f"""Tus intentos son {contador} y 
la suma de los numeros que pusistes es {resultado}""")
        break