"""crear una lista de frutas de 2 elementos y realizar un programa
que muestre una oracion conteniendo los dos elementos
de la lista concatenando con un texto para formsr una oracion"""

fruits = []
for i in range(2):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

sentence = f"Mi mama me ofrecio {fruits[0]}, but I wanted {fruits[1]}."
print(sentence)
