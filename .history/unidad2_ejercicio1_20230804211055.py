"""
El código está importando el módulo `sys`, que proporciona acceso a algunas
variables por el intérprete y a funciones que interactúan
con el intérprete. Este código filtra los números pares de
una lista de números e imprime los números pares
"""


# 1.Importa el módulo sys para obtener argumentos desde la consola línea.

# 2.La función filter_even_numbers filtra una lista de números pares.

# 3.print_even_numbers function imprime una lista de números pares.

# 4.if __name__ == "__main__" ejecuta la lógica del programa principal.

# 5.Obtiene los argumentos desde la consola sys.argv[1:].

# 6.Intenta convertir cada argumento en un entero.

# 7.Añade enteros válidos a la lista de números.

# 8.Imprime error para enteros inválidos.

# 9.Llama a filter_even_numbers para obtener sólo números pares.

# 10.Llama a print_even_numbers para imprimir los números pares.

import sys


def filter_even_numbers(numbers_list):
    """
    Filtra numeros pares desde la lista de enteros.

    Args:
        numbers_list (list): Lista de enteros.

    Returns:
        list: Lista de enteros pares.
    """
    # Crea una nueva lista que contiene sólo los números pares
    return [number for number in numbers_list if number % 2 == 0]


def print_even_numbers(numbers):
    """
    Imprime una lista de numeros pares.

    Args:
        numbers (list): Lista de enteros.
    """
    # Imprime cada número par de la lista
    for number in numbers:
        print(f"{number} es un numero par")


if __name__ == "__main__":
    # Obtener los argumentos desde la consola
    arguments = sys.argv[1:]

    # Convertir los argumentos a enteros
    numbers = []
    for argument in arguments:
        try:
            current_number = int(argument)
            numbers.append(current_number)
        except ValueError:
            print(f"{argument} no es is not a valid integer")

    # Filter even numbers
    even_numbers = filter_even_numbers(numbers)

    # Print even numbers
    print_even_numbers(even_numbers)
