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
    for