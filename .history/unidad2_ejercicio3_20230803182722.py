"""
Prompts user for 2 numeric values, sums them, and returns a list with
the values and sum.

Parameters:
    prompt (str): The prompt to display when requesting input.
    valor1 (float): The first numeric value entered.
    valor2 (float): The second numeric value entered.

Returns:
    list: A list containing the 2 input values and their sum.

Functionality:
    1. Defines get_numeric_input to validate numeric input.
    2. Defines sum_and_list to:
        a. Get 2 numeric values from user input
        b. Sum the values
        c. Return a list containing the values and sum
    3. Prints the returned list.
"""


def get_numeric_input(prompt: float) -> float:
    """obtener valores numericos"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")


def sum_and_list():
    # Solicitar los valores al usuario y guardarlos en variables
    valor1 = get_numeric_input("Ingrese un valor: ")
    valor2 = get_numeric_input("Ingrese otro valor: ")
    # Realizar la suma
    suma = valor1 + valor2
    # Devolver una lista con los valores ingresados y la suma
    return [valor1, valor2, suma]


# Mostrar el resultado
print(sum_and_list())
