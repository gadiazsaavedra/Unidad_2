"""hola"""


def sum_and_list():
    return [float(input("Ingrese un valor: ")) for _ in range(2)] + [
        sum(float(input("Ingrese un valor: ")) for _ in range(2))
    ]
print(sum_and_list())