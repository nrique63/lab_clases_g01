"""diccionarios en python"""
"""del: elimina un key y su valor del diccionario"""
var_1 = {"nombre": "Susana", "edad": 29, "promedio": 14.9}
var_1["distrito"] = "Comas"
del var_1["edad"]
del var_1["promedio"]
print(var_1)