# dame tu nombre que lo guardo en un archivo.txt

nombre = input("Dime tú nombre: ") 
with  open("pruba2.txt", "w") as pruba2: # cuando se abra escribe en
    # otro archivo el nombre puesto
    pruba2.write("Hola, " + nombre)