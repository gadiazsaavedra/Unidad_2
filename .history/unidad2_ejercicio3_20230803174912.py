"""hola"""

def sum_and_list():
    valor1 = float(input("Ingrese un valor: "))
    valor2 = float(input("Ingrese otro valor: "))
    suma = valor1 + valor2
    lista = [valor1, valor2, suma]
    return lista

print(sum_and_list())