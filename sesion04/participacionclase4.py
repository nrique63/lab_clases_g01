""" REQUISITOS
- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensualmenos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"""

var_1 = input("Ingrese el nombre")
var_2 = input("Ingrese el primer apellido")
var_3 = input("Ingrese el distrito donde reside")
var_4 = input("Ingrese el sueldo")
nombre, apellido, distrito, sueldo = var_1, var_2, var_3, var_4
sld = int(sueldo)
bono = sld*3 - 10*sld/100
dic = {}
dic["nombre"] = nombre
dic["apellido"] = apellido
dic["distrito"] = distrito
dic["sueldo"] = sueldo
dic["bono"] = bono
print(dic)
print("{} {} recibira {} soles de bono de fin de año".format(nombre, apellido, bono))
