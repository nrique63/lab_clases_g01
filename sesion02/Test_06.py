"""
Requisitos

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables para la remuneración de enero y febrero (más de 1000)
3. Crear 1 variable deonde se sumará el ingreso de los meses de enero y feberero
4. Mostrar en pantalla el mensaje de:

Mnesaje final:
"Hola soy 'nombre' mi 'profesión' y mi remuneración acumulada es de 'remuneración total'"
"""
nombre= "Enrique"
profesion= "ingeniero de sistemas"
ciudad= "lima"
rEn=1500
rFeb=3200
rTotal=rEn+rFeb
print("Hola soy {}, mi profesion es {} y mi remuneracion acumulada es de {} soles en total".format(nombre,profesion,rTotal))