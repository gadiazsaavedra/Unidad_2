"""ingresar radio de una circunferencia y calcular el perimetro"""

import math


def calcular_perimetro_y_area(radio):
    pi = math.pi
    perimetro = 2 * pi * radio_circunferencia
    area = pi * radio_**2
    return perimetro, area


radio_circunferencia = float(input("Ingresar el radio : "))
perimetro, area = calcular_perimetro_y_area(radio_circunferencia)

print("El perimetro es:", round(perimetro, 2))
print("El area sera:", round(area, 2))

print("En caso el radio aumente un 10%, los valores serian")
radio_circunferencia += radio_circunferencia * 0.1
perimetro, area = calcular_perimetro_y_area(radio_circunferencia)

print("El perimetro es:", round(perimetro, 2))
print("El area sera:", round(area, 2))
