"""ingresar radio de una circunferencia y calcular el perimetro"""


import math


def calcular_perimetro_y_area(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    pi = math.pi
    perimetro = 2 * pi * radio
    area = pi * radio**2
    return perimetro, area


radio_circunferencia = float(input("Ingresar el radio : "))
perimetro, area = calcular_perimetro_y_area(radio_circunferencia)

print("El perimetro es:", round(perimetro, 2))
print("El area sera:", round(area, 2))

print("En caso el radio aumente un 10%, los valores serian")
radio_circunferencia += radio_circunferencia * 0.1
perimetro2, area2 = calcular_perimetro_y_area(radio_circunferencia)

print("El perimetro es:", round(perimetro2, 2))
print("El area sera:", round(area2, 2))
