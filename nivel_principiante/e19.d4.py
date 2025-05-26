# pedimos dato
f1 = input("Dime una frase: ")

# reemplazamos los espacios con nada
f1 = f1.replace(" ", "")
print(len(f1)) # imiprimos el taño de la frase (en caracteres)

print(f1[::-1]) 

# imprimimos la frase dese atras 
# por eso usamos el indice -1

# aloh
# -4-3-2-1
# hola
# 0123