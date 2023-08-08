"""hola"""


def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")


def sum_and_list():
    valor1 = get_numeric_input("Ingrese un valor: ")
    valor2 = get_numeric_input("Ingrese otro valor: ")
    suma = valor1 + valor2
    lista = [valor1, valor2, suma]
    return lista


print(sum_and_list())
