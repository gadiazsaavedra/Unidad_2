"""ingresar radio de una circunferencia y calcular el perimetro"""

import math

pi = math.pi
radio_circunferencia = float(input("Ingresar el radio : "))
longitud_de_perimetro = 2 * pi * radio_circunferencia
area = pi * radio_circunferencia**2

print("El perimetro es:", round(longitud_de_perimetro, 2))
print("El area sera:", round(area, 2))

print("En caso el radio aumente un 10%, los valores serian")
radio_circunferencia += radio_circunferencia * 0.1
longitud_de_perimetro = 2 * pi * radio_circunferencia
area = pi * radio_circunferencia**2

print("El perimetro es:", round(longitud_de_perimetro, 2))
print("El area sera:", round(area, 2))
