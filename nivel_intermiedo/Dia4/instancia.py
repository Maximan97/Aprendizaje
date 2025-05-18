# Creá una clase Rectangulo que tenga atributos base y altura. Agregale 
# un método area() que calcule y retorne el área del rectángulo (base *
#  altura)

class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    def cal_area(self):
        area = self.base * self.altura
        return area

# rectangulo = Rectangulo(3, 5) 
# print(rectangulo.cal_area())