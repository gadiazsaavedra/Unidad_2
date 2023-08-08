"""
El código está importando el módulo `sys`, que proporciona acceso a algunas
variables por el intérprete y a funciones que interactúan
con el intérprete. Este código filtra los números pares de
una lista de números e imprime los números pares

1.Importa el módulo sys para obtener los argumentos de la línea de comandos.

"""


import sys


def filter_even_numbers(numbers_list):
    return [x for x in numbers_list if x % 2 == 0]


def print_even_numbers(numbers):
    for number in numbers:
        print(f"{number} es un numero par")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    numbers = [int(x) for x in arguments if x.isdigit()]
    even_numbers = filter_even_numbers(numbers)
    print_even_numbers(even_numbers)