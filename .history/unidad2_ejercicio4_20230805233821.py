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
