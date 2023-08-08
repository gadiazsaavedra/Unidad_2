"""
Solicita al usuario 2 valores numéricos, los suma y devuelve una lista con
los valores y la suma.

Parámetros:
    prompt (str): El prompt a mostrar cuando se solicita la entrada.
    valor1 (float): El primer valor numérico introducido.
    valor2 (float): El segundo valor numérico introducido.

Devuelve:
    lista: Una lista que contiene los 2 valores introducidos y su suma.

Funcionalidad:
    1. Define get_numeric_input para validar la entrada numérica.
    2. Define sum_and_list para:
        a. Obtener 2 valores numéricos de la entrada del usuario
        b. Sumar los valores
        c. Devuelve una lista que contiene los valores y la suma
    3. Imprime la lista devuelta.
"""


def get_numeric_input(prompt: float) -> float:
    """obtener valores numericos"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")


def sum_and_list():
    """Hacer una lista y sumar los valores make the list and do the sum"""
    # Solicitar los valores al usuario y guardarlos en variables
    valor1 = get_numeric_input("Ingrese un valor: ")
    valor2 = get_numeric_input("Ingrese otro valor: ")
    # Realizar la suma
    suma = valor1 + valor2
    # Devolver una lista con los valores ingresados y la suma
    return [valor1, valor2, suma]


# Mostrar el resultado
print(sum_and_list())
