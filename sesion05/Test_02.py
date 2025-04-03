"""uso del condicional if"""
edad = int(input("Ingrese su edad :"))
if 0 < edad < 18:
    print("usted es menor de edad")
elif 18 <= edad < 65:
    print("usted es una persona adulta")
elif 65<= edad < 100:
    print("usted es una persona de la tercera edad")
else:
    print("usted ha ingresado una edad incorrecta, ingrese nuevamente la edad")
    