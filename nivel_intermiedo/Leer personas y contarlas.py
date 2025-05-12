c = 0

with open("usuarios2.txt", "r") as archivo:
    for linea in archivo:
        c += 1
        print(linea)

print(f"Hay {c} pernosas")