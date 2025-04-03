"""cadenas o strings"""
"""concatenacion"""
nombre = input("ingresa un nombre:")
apellido = input("ingresa un apellido:")
nombre_completo = "El nombre completo del usuario es :" + nombre +  " " + apellido
print(nombre_completo)
nombre_completo2 = "El nombre completo del usuario es :{} {}".format(nombre, apellido)
print(nombre_completo2)
