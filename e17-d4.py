#uso rangue para evitarme poner ,uchos numeros

n1 = int(input("Didme la hora: "))

if n1 > 24 or n1 < 0:
    print("ingresa algo valido")
    exit()

if n1 in range(6, 12):
    print("BON JORNO")
elif n1 in range(12, 20):
    print("bona sera")
if n1 in range(20, 24) or n1 in range(0,6):
    print("bona noite")