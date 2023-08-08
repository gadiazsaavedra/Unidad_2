"""hola"""


def get_numeric_input(prompt: float) -> float:
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
