n1 = int(input("Didme la nota: "))

# esta´+s pidiendo edad

if n1 > 11 or n1 < 0:
    print("ingresa algo valido")
    exit()


if n1 in [9, 10]:
    print("Exelente.")
elif n1 in [7, 8]:
    print("Muy bien.")
elif n1 in [6]:
    print("Bien.")
else:
    print("sigue estudiando.")