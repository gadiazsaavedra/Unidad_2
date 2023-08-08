"""ingresar radio de una circunferencia y calcular el perimetro"""


import math


def calcular_perimetro(radio):
    pi = math.pi
    perimetro = 2 * pi * radio
    return perimetro


def calcular_area(radio):
    pi = math.pi
    area = pi * radio**2
    return area


def calcular_perimetro_y_area(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    perimetro = calcular_perimetro(radio)
    area = calcular_area(radio)
    return perimetro, area


while True:
    radio_circunferencia = input("Ingresar el radio : ")
    try:
        radio_circunferencia = float(radio_circunferencia)
    except ValueError:
        print("Error: el valor ingresado no es numerico")
        continue
    try:
        perimetro, area = calcular_perimetro_y_area(radio_circunferencia)
    except ValueError as e:
        print("Error:", e)
        continue
    break

print("El perimetro es:", round(perimetro, 2))
print("El area sera:", round(area, 2))

print("En caso el radio aumente un 10%, los valores serian")
radio_circunferencia += radio_circunferencia * 0.1
perimetro2, area2 = calcular_perimetro_y_area(radio_circunferencia)

print("El perimetro es:", round(perimetro2, 2))
print("El area sera:", round(area2, 2))
