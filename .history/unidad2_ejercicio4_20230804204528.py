"""
Solicita al usuario la edad y el sexo para determinar el derecho a la jubilación.

Parámetros:
    prompt (str): Preguntar al usuario
    valid_values (lista): Valores válidos para el usuario
    retirement_age_limits (dict): Edad de jubilación por sexo
    edad_usuario (int): Edad del usuario
    sexo_usuario (str): Sexo del usuario ('m' o 'f')

Devuelve:
    Ninguno: Imprime mensajes de salida en lugar de devolver valores

Funcionalidad:
    1. validate_input pregunta al usuario hasta que la entrada es válida
    2. main:
        a. Validar los límites de edad de jubilación
        b. Obtener la edad del usuario con validación de entrada
        c. Obtener el sexo del usuario con validate_input
        d. Comprobar el derecho a la jubilación
        e. Imprimir mensaje de salida

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator"""


def validate_input(prompt, valid_values):
    """
    Prompts the user for input until they enter a valid value.

    Args:
        prompt (str): The prompt to display to the user.
        valid_values (list): A list of valid values.

    Returns:
        str: The user's input (lowercased).
    """
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            print("Debe indicar el sexo...!!")
        elif user_input.lower() in valid_values:
            return user_input.lower()
        else:
            print(
                f"Input invalido. Los valores validos son ({', '.join(valid_values)})"
            )


def main():
    retirement_age_limits = {"m": 65, "f": 60}

    # Validate retirement age limits
    for gender, age in retirement_age_limits.items():
        if not isinstance(age, int) or age < 0:
            raise ValueError(f"Edad limite invalida para {gender}: {age}")

    while True:
        try:
            edad_usuario = int(input("Ingrese su edad: "))
            if edad_usuario < 0:
                raise ValueError("La edad debe ser un número positivo")
            break
        except ValueError:
            print("La edad debe ser un número entero positivo")

    sexo_usuario = validate_input("Ingrese su sexo (m/f): ", ["m", "f"])

    if (sexo_usuario == "m" and edad_usuario < retirement_age_limits["m"]) or (
        sexo_usuario == "f" and edad_usuario < retirement_age_limits["f"]
    ):
        print("Aun esta en edad de trabajar")
    else:
        print("Ya esta en edad de jubilarse")


if __name__ == "__main__":
    main()
