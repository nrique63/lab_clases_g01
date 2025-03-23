"""
Requisitos

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string
con contenido solamente numérico y 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(realizar conversiones si es necesario)
3. Obtener y mostar la suma de las 2 variables enteras más la variable string numérica y la
variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostarar el resultado entero o la parte entera de las 2 variables int: //
6. Obtener una potencia usando una de las variables flotantes como base y la variable entera como potencia
"""
#I.
ent1 = 4
ent2 = 12
flot1 = 11.23
flot2 = 5.84
strin1 = "Enrique"
strin2 = "2131"
boo = True
# II.
intstrin2 = int(strin2)
suma_01 = ent1 + intstrin2
print(suma_01)
#III.
suma_02 = ent1 + ent2 + intstrin2 + flot1
print(suma_02)
#IV.
faf = ent2 % ent1
print(faf)
#V.
rar = ent2 // ent1
print(rar)
#VI.
pot = flot1** ent2
print(pot)


