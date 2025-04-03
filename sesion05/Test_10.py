"""metodos de separacion de cadenas a strings"""

"""metodos de separacion de strings: split()"""

cadena = "Python para la prediccion de fraudes bancarios"
cadena_sin_espacios = cadena.split()
print("cadena separada por espacios en blanco dentro del string:{}".format(cadena_sin_espacios))
for palabra in cadena_sin_espacios:
    print(palabra)