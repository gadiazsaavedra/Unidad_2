"""hola"""

while True:
    try:
        edad_usuario = int(input("Ingrese su edad: "))
        if edad_usuario < 0:
            raise ValueError("La edad debe ser un número positivo")
        break
    except ValueError:
        print("La edad debe ser un número entero positivo")

while True:
    sexo_usuario = input("Ingrese su sexo (m/f): ")
    if sexo_usuario.lower() not in ["m", "f"]:
        print("El sexo debe ser 'm' o 'f'")
    else:
        break

if sexo_usuario == "m" and edad_usuario < 65:
    print("Ud debe seguir trabajando")
elif sexo_usuario == "f" and edad_usuario < 60:
    print("Ud debe seguir trabajando")
else:
    print("Ud se puede jubilar")
