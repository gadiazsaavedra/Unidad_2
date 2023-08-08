"""
1.Define una función validate_input que:

    Toma como parámetros un prompt y una lista de valores válidos

Utiliza un while para preguntar repetidamente al usuario hasta que introduzca un valor válido

Devuelve la entrada válida en minúsculas

Define una función principal que:

Establece un diccionario con los límites de edad de jubilación por sexo

Valida que los límites de edad de jubilación sean enteros válidos

Utiliza un bloque try/except para validar que la edad introducida por el usuario es un entero positivo

Llama a validate_input para obtener una entrada 'm' o 'f' válida para el género

Comprueba las normas de jubilación en función de la edad y el sexo.

Imprime si el usuario cumple los requisitos para jubilarse o no

Ejecuta la función principal si se ejecuta como script

En general:

validate_input pregunta repetidamente hasta obtener una entrada válida

main obtiene la edad y el sexo con validación, comprueba las reglas de elegibilidad e imprime los resultados

El código ejecuta el flujo de trabajo completo para determinar la elegibilidad para la jubilación
"""


def validate_input(prompt, valid_values):
    """
    Pregunta al usuario hasta que introduce un valor válido.

    Args:
        prompt (str): El prompt a mostrar al usuario.
        valid_values (lista): Lista de valores válidos.

    Devuelve:
        str: La entrada del usuario (en minúsculas).
    """
    # Utiliza una expresión while para pedir al usuario que ingrese un valor válido
    user_input = ""
    while user_input.strip() == "" or user_input.lower() not in valid_values:
        user_input = input(prompt).lower()
        if user_input.strip() == "":
            print("Debe indicar el sexo...!!")
        elif user_input.lower() not in valid_values:
            print(
                f"Input invalido. Los valores validos son ({', '.join(valid_values)})"
            )
    return user_input


def main():
    retirement_age_limits = {"m": 65, "f": 60}

    # Validar edad limite de jubilación
    if not all(isinstance(age, int) and age >= 0 for age in retirement_age_limits.values()):
        raise ValueError("Edad limite invalida")

    # Utiliza una expresión try-except para validar la entrada de edad del usuario
    while True:
        try:
            edad_usuario = int(input("Ingrese su edad: "))
            if edad_usuario < 0:
                raise ValueError("La edad debe ser un número positivo")
            break
        except ValueError:
            print("La edad debe ser un número entero positivo")

    sexo_usuario = validate_input("Ingrese su sexo (m/f): ", ["m", "f"])

    # Utiliza una expresión if-else para determinar si el usuario está en edad de jubilarse
    if (sexo_usuario == "m" and edad_usuario < retirement_age_limits["m"]) or (
        sexo_usuario == "f" and edad_usuario < retirement_age_limits["f"]
    ):
        print("Aun esta en edad de trabajar")
    else:
        print("Ya esta en edad de jubilarse")


if __name__ == "__main__":
    main()
