import math


def calculate_perimeter(radius):
    pi = math.pi
    perimeter = 2 * pi * radius
    return perimeter


def calculate_area(radius):
    pi = math.pi
    area = pi * radius**2
    return area


def calculate_perimeter_and_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    perimeter = calculate_perimeter(radius)
    area = calculate_area(radius)
    return perimeter, area


while True:
    circle_radius = input("Enter the radius: ")
    try:
        circle_radius = float(circle_radius)
    except ValueError:
        print("Error: the input is not numeric")
        continue

    try:
        perimeter, area = calculate_perimeter_and_area(circle_radius)
    except ValueError as e:
        print("Error:", e)
        continue

    break

print("The perimeter is:", round(perimeter, 2))
print("The area will be:", round(area, 2))

print("If the radius increases 10%, the values would be:")
circle_radius += circle_radius * 0.1
perimeter2, area2 = calculate_perimeter_and_area(circle_radius)

print("The perimeter is:", round(perimeter2, 2))
print("The area will be:", round(area2, 2))
