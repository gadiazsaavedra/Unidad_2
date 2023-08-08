"""hola"""
edad_usuario = int(input("Ingrese su edad : "))
sexo_usuario = input("ingrese su sexo (m/f)")
if sexo_usuario == "m" and edad_usuario < 65:
    print("Ud debe seguir trabajando")
elif sexo_usuario == "f" and edad_usuario < 60:
    print("Ud debe seguir trabajando")
else:
    print("Ud se puede jubilar")
