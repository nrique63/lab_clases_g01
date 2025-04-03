"""if ternarios"""
"""
Requisitos: 
 - Ingresar por teclado el sueldo de un empleado
 - Si el sueldo es mayor a 2500 y menor a 3500, imprimir "Su sueldo no tiene bonificación"
 y se le agregará el 10%, para luego mostrar el sueldo final con la bonificación
 - Caso contrario: "Su sueldo tiene bonificación este año y será de: 
 'sueldo_final'", sueldo_final= sueldo + 2% sueldo
"""
sueldo = int(input("Ingrese su sueldo"))
porcen = 10*sueldo/100
sueldo_final = sueldo + 2*sueldo/100
if 2500 < sueldo < 3500:
    print("Su sueldo no tiene bonificacion")
    print("Su sueldo final es de", sueldo + porcen, "más bonificación")
else:
    print("Su sueldo tiene bonificacion este año y será de:", sueldo_final)