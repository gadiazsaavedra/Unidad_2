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
            print("Input cannot be empty.")
        elif user_input.lower() in valid_values:
            return user_input.lower()
        else:
            print(f"Invalid input. Valid values are {', '.join(valid_values)}")


def main():
    retirement_age_limits = {"m": 65, "f": 60}

    # Validate retirement age limits
    for gender, age in retirement_age_limits.items():
        if not isinstance(age, int) or age < 0:
            raise ValueError(f"Invalid retirement age limit for {gender}: {age}")

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
        print("Ud debe seguir trabajando")
    else:
        print("Ud se puede jubilar")


if __name__ == "__main__":
    main()
