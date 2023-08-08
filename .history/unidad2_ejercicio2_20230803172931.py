"""crear una lista de frutas de 2 elementos y realizar un programa
que muestre una oracion conteniendo los dos elementos
de la lista concatenando con un texto para formsr una oracion"""

fruits = []
for i in range(2):
    while True:
        fruit = input(f"Escribir una fruta {i+1}: ")
        if not fruit.isalpha():
            print("Error: La entrada debe ser una cadena de texto que contenga solo letras.")
        else:
            fruits.append(fruit)
            break

sentence = f"Mi mama me ofrecio {fruits[0]}, pero yo queria {fruits[1]}."
print(sentence)