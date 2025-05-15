# 1) Crea una clase llamada Vehiculo. Por ahora, no tiene que hacer 
# nada (una clase vacía). Solo definila y asegurate de que Python la 
# reconozca sin errores.
# 2) Creá un objeto llamado mi_auto
# Creá un segundo objeto llamado tu_auto
# Imprimí sus tipos para confirmar que son objetos (print(type(mi_auto)))
# 3) Ampliá la clase Vehiculo para que:
# Tenga un __init__ que reciba marca y modelo
# Guarde esos datos en self.marca y self.modelo

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_auto = Vehiculo
tu_auto = Vehiculo

print(type(mi_auto))
print(type(tu_auto))

f1 = Vehiculo("Ferrari", "SF500")
mugtan = Vehiculo("Mugtan", "GT")

print(f1.marca + " " + f1.modelo)
print(mugtan.marca + " " + mugtan.modelo)