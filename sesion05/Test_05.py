"""uso del condicional for"""
ingenierias = ["sistemas", "software", "industrial", "civil", "mecanica", "mecatronica"]
print("El tamaño de la lista es:{}".format(len(ingenierias)))

i = 0
for ingenieria in ingenierias:
     print("Ingenieria {}".format(ingenieria))
     print("valor de i: {}".format(i))

     if i == 2:
         ingenierias[i] = "Estadistica"
     i = i +1


print("la lista actualizada es :{}".format(ingenierias))
