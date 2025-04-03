"""usando los metodos de cadenas o strings"""

"""metodos de strings"""
cadena = "Conexion a base de datos con python"
cadena2= cadena.replace(cadena[0:8], "Nueva conexion")    #posicion de caracteres, el 8 no agarra
print("cadena con reemplazo tiene el siguiente valor actualizado :{}".format(cadena2))

"""eliminacion de espacios en blanco de mi cadena(despues)"""
cadena_3 = "conexion a base de datos con python     "
cadena_4 = cadena_3.rstrip()
print(cadena_3)
print("Mi cadena actualizada sin espacios es :{}".format(cadena_4))

"""eliminacion de espacios en blanco de mi cadena(antes)"""
cadena_5 = "        conexion a base de datos con python"
cadena_6 = cadena_5.rstrip()

