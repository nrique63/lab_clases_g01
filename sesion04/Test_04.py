"""diccionarios en python"""
"""convirtiendo diccionario a list"""
var_1 = {"nombre": "MYSQL", "tipo": "BD relacional"}
var_2 = list(var_1)
print("mi diccionario queda convertido en: {}".format(var_2))

var_1_values = list(var_1.values())
print(var_1_values)

keys = list(var_1.keys())
print(keys)

var_3 = list(var_1.items())
print(var_3)