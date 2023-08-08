# sourcery skip: require-parameter-annotation
"""The code is importing the `sys` module, which provides access to some
variables by the interpreter and to functions that interact
with the interpreter.
This code filters the even numbers from a list of numbers
# and prints the even numbers
# """

# 

# 

# Here is an explanation of the Unidad2_ejercicio1.py code:

# 1.Imports the sys module to get command line arguments.

# 2.filter_even_numbers function filters a list for even numbers.

# 3.print_even_numbers function prints a list of even numbers.

# 4.if __name__ == "__main__" runs the main program logic.

# 5.Gets command line arguments from sys.argv[1:].

# 6.Tries to convert each argument to an integer.

# 7.Appends valid integers to the numbers list.

# 8.Prints error for invalid integers.

# 9.Calls filter_even_numbers to get only even numbers.

# 10.Calls print_even_numbers to print the even numbers.
import sys


def filter_even_numbers(numbers_list):
    """
    Filters even numbers from a list of integers.

    Args:
        numbers_list (list): A list of integers.

    Returns:
        list: A list of even integers.
    """
    return [number for number in numbers_list if number % 2 == 0]


def print_even_numbers(numbers):
    """
    Prints a list of even numbers.

    Args:
        numbers (list): A list of integers.
    """
    for number in numbers:
        print(f"{number} is an even number")


if __name__ == "__main__":
    # Get command line arguments
    arguments = sys.argv[1:]

    # Convert arguments to integers
    numbers = []
    for argument in arguments:
        try:
            current_number = int(argument)
            numbers.append(current_number)
        except ValueError:
            print(f"{argument} is not a valid integer")

    # Filter even numbers
    even_numbers = filter_even_numbers(numbers)

    # Print even numbers
    print_even_numbers(even_numbers)
