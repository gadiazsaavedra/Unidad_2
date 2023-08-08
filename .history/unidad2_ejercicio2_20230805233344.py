"""
1.Crea una lista vacía llamada fruits para almacenar los nombres de frutas introducidos por el usuario.

2.Inicializa una variable contador i a 0. Se utilizará para controlar el número de iteraciones.

3.Inicia while que iterará 2 veces (cuando i < 2).

4.En cada iteración:

    .-Imprime un prompt para pedir al usuario que introduzca el nombre de una fruta usando el formato f-string (f "Escribir una fruta {i+1}:"). El {i+1} inserta el valor de i + 1 para numerar los mensajes.

    .-Lee la entrada del usuario en una variable llamada fruta.

    .-Valida si fruta contiene sólo caracteres alfabéticos usando .isalpha().

    .-Si la validación falla, imprime un mensaje de error.

    .-Si la validación pasa, añade fruta a la lista de frutas.

    .-Incrementa i en 1.

1.Luego, crea una sentencia usando el formato f-string con las dos frutas almacenadas en fruits[0] y fruits[1].

2.Imprime la sentencia.

En general, pide al usuario que introduzca dos nombres de frutas, los almacena en una lista e imprime una sentencia utilizando esas frutas. El bucle while itera dos veces para obtener las dos entradas. La validación de la entrada se realiza para comprobar si hay cadenas alfabéticas.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
"""


fruits = []
i = 0
while i < 2:
    fruit = input(f"Escribir una fruta {i+1}: ")
    if not fruit.isalpha():
        print(
            "Error: La entrada debe ser una cadena de texto que contenga solo letras."
        )
    else:
        fruits.append(fruit)
        i += 1

sentence = f"Mi mama me ofrecio {fruits[0]}, pero yo queria {fruits[1]}."
print(sentence)
