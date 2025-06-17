# Concepto 3: Uso de módulos externos (con pip)
# 📘 ¿Qué es?

# Hay módulos creados por otras personas que podés instalar usando pip, 
# el sistema de paquetes de Python.

# Ejercicio 3 – Practicar

#    Instalá el módulo pyjokes con pip.

#    Creá un script que muestre un chiste aleatorio en consola.

#    TIP: pip install pyjokes
#    Luego usá:
#    import pyjokes
#    print(pyjokes.get_joke())

import pyjokes

print(pyjokes.get_joke())