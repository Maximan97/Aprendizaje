# crear un archivo .tex y luego abrirlo 

with open("pruba.tex", "r") as prueba:  # open(tex, r) abre un archivo 
    # y lo "lee"/muestra en pantalla
    for lineas in prueba:
        print(lineas)