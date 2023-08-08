"""crear una lista de frutas de 2 elementos y realizar un programa
que muestre una oracion conteniendo los dos elementos
de la lista concatenando con un texto para formsr una oracion"""


fruits = []
for i in range(2):
    while True:
        fruit = input(f"Escribir una fruta {i+1}: ")
        if not isinstance(fruit, str):
            print("Error: La entrada debe ser una cadena de texto.")
        else:
            fruits.append(fruit)
            break

numbers = []
for i in range(2):
    while True:
        number = input(f"Escribir un numero {i+1}: ")
        if not number.isdigit():
            print("Error: La entrada debe ser un numero entero.")
        else:
            numbers.append(int(number))
            break

sentence = f"Mi mama me ofrecio {fruits[0]}, pero yo queria {fruits[1]}."
print(sentence)

total = sum(numbers)
print(f"La suma de los numeros es: {total}")