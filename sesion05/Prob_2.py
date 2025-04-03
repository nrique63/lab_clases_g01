"""Usando las propiedades de cadenas o string"""
"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
"""
nombre = input("Ingresa tu nombre")
apellido = input("Ingresa tu apellido")
nombre_completo = nombre + " " + apellido
print("El nombre completo es :{}".format(nombre_completo))
print("El tamaño de mi nombre sin contar el espacio es de : {}".format(len(nombre_completo) - 1))
print("El nombre completo en mayúsculas es :{}".format(nombre_completo.upper()))
if len(nombre) < len(apellido):
    print("El tamaño del nombre es menor que el del apellido")
else:
    print("El tamaño del apellido es menor que el nombre")
