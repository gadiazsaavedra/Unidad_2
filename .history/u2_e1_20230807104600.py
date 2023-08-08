"""
El código está importando el módulo `sys`, que proporciona acceso a algunas
variables por el intérprete y a funciones que interactúan
con el intérprete. Este código filtra los números pares de
una lista de números e imprime los números pares

1.Importa el módulo sys para obtener los argumentos de la línea de comandos.

"""


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
    return list(filter(lambda x: x % 2 == 0, numbers_list))


def print_even_numbers(numbers):
    """
    Imprime una lista de numeros pares.

    Args:
        numbers (list): Lista de enteros.
    """
    # Imprime cada número par de la lista
    print("\n".join(map(lambda x: f"{x} es un numero par", numbers)))


if __name__ == "__main__":
    # Obtener los argumentos desde la consola
    arguments = sys.argv[1:]

    # Convertir los argumentos a enteros
    numbers = list(map(lambda x: int(x), filter(lambda x: x.isdigit(), arguments)))

    # Filtrar numeros pares
    even_numbers = filter_even_numbers(numbers)

    # Imprimir numeros pares
    print_even_numbers(even_numbers)
