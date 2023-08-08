"""
El código está importando el módulo `sys`, que proporciona acceso a algunas
variables por el intérprete y a funciones que interactúan
con el intérprete. Este código filtra los números pares de
una lista de números e imprime los números pares

1.Importa el módulo sys para obtener los argumentos de la línea de comandos.

"""


import sys


def filter_even_numbers(numbers_list):
    even_numbers = []
    i = 0
    while i < len(numbers_list):
        if numbers_list[i] % 2 == 0:
            even_numbers.append(numbers_list[i])
        i += 1
    return even_numbers


def print_even_numbers(numbers):
    i = 0
    while i < len(numbers):
        print(f"{numbers[i]} es un numero par")
        i += 1


if __name__ == "__main__":
    arguments = sys.argv[1:]
    numbers = []
    i = 0
    while i < len(arguments):
        if arguments[i].isdigit():
            numbers.append(int(arguments[i]))
        i += 1
    even_numbers = filter_even_numbers(numbers)
    print_even_numbers(even_numbers)
