"""uso del condicional if"""
edad_1 = int(input("Ingrese una primera edad :"))
edad_2 = int(input("Ingrese una segunda edad :"))

if edad_1 < 0 or edad_2 < 0:
    print("Debe ingresar edades positivas")
if edad_1 > edad_2:
    print("La primera edad es mayor que la segunda")
elif edad_2 == edad_1:
    print("Las edades ingresadas son iguales")
else:
    print("La segunda edad es mayor que la primera")