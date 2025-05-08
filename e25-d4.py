numero = int(input("Dame un numero: "))

if not numero > 1:
    print("El número debe ser mayor que cero.")
    exit()

for i in range(1, numero):
    print(i)