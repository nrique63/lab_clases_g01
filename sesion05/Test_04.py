"""uso del condicional while"""
numero = int(input("Cuantos saludos desea enviar :"))
while numero < 10:
    print(numero)
    numero = numero + 1
    #el numero aumento una unidad
    print("El numero con nuevo valor es :{}".format (numero))
    