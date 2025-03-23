"""Listas en Python"""

"""
Requisitos:

- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índica
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente

"""
lis1 = []
lis2 = []
lis1.append("Nelson")
lis1.append(18)
lis1.append("ingeniero de sistemas")

lis2.append("Juan")
lis2.append(34)
lis2.append("abogado")
sumaedades = lis1[1] + lis2[1]
print("La suma de las edades es :{}".format(sumaedades))
print(lis1)
print(lis2)
sum = lis1 + lis2
print("La suma de listas es:{}".format(sum))
lis1.reverse()
lis2.reverse()
print("La lista 1 al reves es :{}".format(lis1))
print("La lista 2 al reves es :{}".format(lis2))
sumainversa = lis1 + lis2
print("la suma inversa de listas es:{} ".format(sumainversa))
lis1.pop(1)
lis2.pop(1)
print("La lista 1 sin edad es :{}".format(lis1))
print("La lista 2 sin edad es :{}".format(lis2))
lis2.clear()
print("La actualizada lista 2 es:{}".format(lis2))