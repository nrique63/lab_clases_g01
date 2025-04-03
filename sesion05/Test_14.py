"""uso del metodo random"""
import random
numero = random.randint(1, 100)
print(numero)
mi_lista = []
for elemento in range(1, 10):
    elemento = random.randint(1, 30)
    mi_lista.append(elemento)

print("Mi lista actualizada tiene los siguientes valores :{}".format(mi_lista))