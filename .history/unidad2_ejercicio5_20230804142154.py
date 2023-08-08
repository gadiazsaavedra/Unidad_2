import math
import re


def calculate_perimeter(radius):
    pi = math.pi
    perimeter = 2 * pi * radius
    return perimeter


def calculate_area(radius):
    pi = math.pi
    area = pi * math.pow(radius, 2)
    return area


def calculate_perimeter_and_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    perimeter = calculate_perimeter(radius)
    area = calculate_area(radius)
    return perimeter, area


def is_numeric(value):
    return bool(re.match(r"^-?\d+(?:\.\d+)?$", value))


while True:
    circle_radius = input("Enter the radius: ")
    if not is_numeric(circle_radius):
        print("Error: the input is not numeric")
        continue

    circle_radius = float(circle_radius)

    try:
        perimeter, area = calculate_perimeter_and_area(circle_radius)
    except ValueError as e:
        print("Error:", e)
        continue

    break

print(f"The perimeter is: {perimeter:.2f}")
print(f"The area will be: {area:.2f}")

print("If the radius increases 10%, the values would be:")
circle_radius += circle_radius * 0.1
perimeter2, area2 = calculate_perimeter_and_area(circle_radius)

print(f"The perimeter is: {perimeter2:.2f}")
print(f"The area will be: {area2:.2f}")
