"""Reconocimiento de tipo de datos:  type()"""
"""Creacion de variables"""
nombre = "Enrique"
ciudad = "Lima"
saldo = 6000
empresa = False
correo = "enriques@gmail.com"
empleado =[nombre, saldo, empresa, ciudad]
empleado_dic = {'nomb': nombre, 'ciud' : ciudad, 'sald': saldo, 'empre': empresa, 'corr': correo}
print("Tipo de dato de mi variable 'nombre' es : {}".format(type(nombre)))
print("Tipo de dato de mi variable 'ciudad'es : {}".format(type(ciudad)))
print("Tipo de dato de mi variable 'saldo': {}".format(type(nombre)))
print("Tipo de dato de mi variable 'empresa'{}".format(type(nombre)))
print("Tipo de dato de mi variable 'correo' es : {}".format(type(correo)))