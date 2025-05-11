nombre = input("Dime tú nombre: ") 
with  open("pruba2.txt", "a") as pruba2:
    pruba2.write(nombre + "\n")