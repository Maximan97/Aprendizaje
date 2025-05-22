# Explicación:

# A veces querés sobrescribir un método, pero también usar la lógica 
# del padre.
# Podés hacer esto con super().metodo().

# Esto es útil cuando querés extender un comportamiento, no 
# reemplazarlo totalmente.

# Ejercicio 3 – Practicar:

# Creá una clase Usuario con un método presentarse() que diga su nombre.
# Luego una clase Admin que lo sobrescriba, pero también use el método 
# original con super() y agregue "Soy administrador.".

class Usuario():
    def presentarse(self):
        print("NENA DI TU NOMBRE")

class Admin(Usuario):
    def presentarse(self):
        super().presentarse()
        print("Soy admin")

