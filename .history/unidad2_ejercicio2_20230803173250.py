"""
Prompts user to input 2 fruit names, stores them in a list, 
and prints a sentence using the fruits.

Parameters:
    fruits (list): The list to store the fruit names.
    i (int): The loop counter variable. 
    fruit (str): The user input fruit name.

Returns:
    None: Prints the result sentence instead of returning.

Functionality:
    1. Initialize empty fruits list
    2. Loop 2 times to get 2 fruits:
        a. Prompt user for fruit name input
        b. Validate input is alphabetic string
        c. Append valid fruit to fruits list
    3. Build sentence using format string with fruits[0] and fruits[1]
    4. Print the sentence
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
