"""hola"""


def sum_and_list():
    while True:
        try:
            valor1 = float(input("Ingrese un valor: "))
            valor2 = float(input("Ingrese otro valor: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    suma = valor1 + valor2
    lista = [valor1, valor2, suma]
    return lista

print(sum_and_list())