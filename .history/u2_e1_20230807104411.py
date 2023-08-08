"""
El código está importando el módulo `sys`, que proporciona acceso a algunas
variables por el intérprete y a funciones que interactúan
con el intérprete. Este código filtra los números pares de
una lista de números e imprime los números pares

"""


import sys


def filter_even_numbers(numbers_list):
    return list(filter(lambda x: x % 2 == 0, numbers_list))


def print_even_numbers(numbers):
    print("\n".join(map(lambda x: f"{x} es un numero par", numbers)))


if __name__ == "__main__":
    arguments = sys.argv[1:]
    numbers = list(map(lambda x: int(x), filter(lambda x: x.isdigit(), arguments)))
    even_numbers = filter_even_numbers(numbers)
    print_even_numbers(even_numbers)
