"""hola"""


def get_numeric_input(prompt: A):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")


def sum_and_list():
    valor1 = get_numeric_input("Ingrese un valor: ")
    valor2 = get_numeric_input("Ingrese otro valor: ")
    suma = valor1 + valor2
    return [valor1, valor2, suma]


print(sum_and_list())
