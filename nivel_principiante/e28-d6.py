clave = "salir"

while True:
    opcion = input("Dime la clave: ")
    if len(opcion) > 3: # Opcion debe ser mayor d 3 "letra"
        if opcion != clave: # compara 
            print("incorrectop") 
            continue
        else: # olvide para que se usa
            print("correctop")
            break # termina el buclee