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
        numbers_list (list): ist of integers.

    Returns:
        list: A list of even integers.
    """
    # Creates a new list containing only the even numbers
    return [number for number in numbers_list if number % 2 == 0]


def print_even_numbers(numbers):
    """
    Prints a list of even numbers.

    Args:
        numbers (list): A list of integers.
    """
    # Prints each even number in the list
    for number in numbers:
        print(f"{number} is an even number")


if __name__ == "__main__":
    # Get command line arguments
    arguments = sys.argv[1:]

    # Convert arguments to integers
    numbers = []
    for argument in arguments:
        try:
            current_number = int(argument)
            numbers.append(current_number)
        except ValueError:
            print(f"{argument} is not a valid integer")

    # Filter even numbers
    even_numbers = filter_even_numbers(numbers)

    # Print even numbers
    print_even_numbers(even_numbers)
