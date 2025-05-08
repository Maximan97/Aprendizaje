# usando not, or, and
dad = int(input("Dime tu edad: "))

if not dad >= 18: # Si es meno
    print("no puedes votar")
    exit()

nacionalidad = input("Dime tu nacionalidad: ")

if nacionalidad.lower() != "argentina": #si no argentino
    print("NO puedes votar")
    exit()

if dad >= 18 and nacionalidad.lower() == "argentina": 
    print("puedes votar.")