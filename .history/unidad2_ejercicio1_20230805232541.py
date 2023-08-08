"""
El código está importando el módulo `sys`, que proporciona acceso a algunas
variables por el intérprete y a funciones que interactúan
con el intérprete. Este código filtra los números pares de
una lista de números e imprime los números pares

1.Importa el módulo sys para obtener los argumentos de la línea de comandos.

2.Define una función filter_even_numbers que:

    .-Toma una lista de números como entrada
    .-Utiliza filter() y lambda para crear una nueva lista con sólo los números pares
    .-Devuelve la lista de números pares

3.Define una función print_even_numbers que:

    .-Toma una lista de números como entrada
    .-Utiliza map() y lambda para crear una lista de cadenas que representen cada número par
    .-Une la lista de cadenas con nuevas líneas y la imprime

4.La lógica principal:

    .-Obtiene los argumentos de sys.argv[1:]
    .-Utiliza map() y lambda para convertir los argumentos en enteros
    .-Filtra para mantener sólo enteros válidos (descarta los no dígitos)
    .-Llama a filter_even_numbers para obtener sólo los números pares
    .-Llama a print_even_numbers para imprimir los números pares

5.La comprobación de nombres ejecuta la lógica principal si se ejecuta como un script.

En general, toma argumentos de la línea de comandos, filtra
los argumentos no enteros, filtra sólo los enteros pares y los imprime.
Utiliza map(), filter() y funciones lambda para transformar y filtrar los datos.
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
