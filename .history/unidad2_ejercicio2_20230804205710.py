"""
Pide al usuario que introduzca 2 nombres de frutas, los almacena en una lista,
e imprime una frase usando las frutas.

Parámetros:
    frutas (lista): La lista para almacenar los nombres de las frutas.
    i (int): La variable contadora del bucle.
    fruit (str): El nombre de la fruta introducido por el usuario.

Devuelve:
    Ninguno: Imprime la frase resultante.

Funcionalidad:
    1. Inicializa la lista de frutas vacía
    2. Hacer el bucle 2 veces para obtener 2 frutas:
        a. Pedir al usuario que introduzca el nombre de la fruta
        b. Validar si la entrada es una cadena alfabética
        c. Añadir la fruta válida a la lista de frutas
    3. Construir la frase usando formato en cadena con frutas[0] y frutas[1]
    4. Imprimir la frase
"""


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
