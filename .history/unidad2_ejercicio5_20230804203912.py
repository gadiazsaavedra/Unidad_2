"""
Calcula e imprime el perímetro y el área de un círculo dado el radio.

Parámetros:
  radio (float): El radio del círculo.

Devuelve:
  Ninguno: Los resultados se imprimen en lugar de devolverse.

Funcionalidad:

  1. validate_input valida la entrada numérica del usuario

  2. calculate_perimeter calcula el perímetro para un radio dado

  3. calculate_area calcula el área para un radio dado  

  4. calculate_perimeter_and_area llama a las funciones de cálculo y gestiona las entradas no válidas

  5. print_results imprime los resultados de perímetro y área

  6. print_results_with_increase imprime los resultados para el radio original e incrementado

  7. main llama a las otras funciones para:
  
     a. Obtener el radio válido del usuario
  
     b. Imprimir los resultados originales
  
     c. Imprimir resultados con 10% de incremento

  8. El script ejecuta la función principal si se ejecuta directamente
"""


import math
import re


def calculate_perimeter(radius):
    pi = math.pi
    perimeter = 2 * pi * radius
    return perimeter


def calculate_area(radius):
    pi = math.pi
    area = pi * math.pow(radius, 2)
    return area


def calculate_perimeter_and_area(radius):
    if radius < 0:
        raise ValueError("El radio NO puede ser negativo")
    perimeter = calculate_perimeter(radius)
    area = calculate_area(radius)
    return perimeter, area


def is_numeric(value):
    return bool(re.match(r"^-?\d+(?:\.\d+)?$", value))


def get_radius():
    while True:
        circle_radius = input("Ingresar el radio : ")
        if not is_numeric(circle_radius):
            print("Error: lo ingresado no es numerico ")
            continue

        circle_radius = float(circle_radius)

        try:
            calculate_perimeter_and_area(circle_radius)
        except ValueError as e:
            print("Error:", e)
            continue

        return circle_radius


def print_results(perimeter, area):
    print(f"El perimetro es : {perimeter:.2f}")
    print(f"El area The area will be: {area:.2f}")


def print_results_with_increase(radius, increase_percent):
    perimeter, area = calculate_perimeter_and_area(radius)
    print_results(perimeter, area)

    print(f"If the radius increases {increase_percent}%, the values would be:")
    circle_radius = radius + radius * increase_percent / 100
    perimeter2, area2 = calculate_perimeter_and_area(circle_radius)
    print_results(perimeter2, area2)


def main():
    radius = get_radius()
    print_results_with_increase(radius, 10)


if __name__ == "__main__":
    main()
