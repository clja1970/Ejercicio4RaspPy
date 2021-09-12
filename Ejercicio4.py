
provincias = ["Almeria","Sevilla", "Cordoba", "Cadiz", "Granada", "Malaga", "Huelva", "Jaen"]
gentilicios = ["Almeriense","Sevillano", "Cordobee", "Pisha", "Granaino", "Malagueño", "Onubense", "Jienense"]
for p in provincias:
    print (p, end =", ")
    
respuesta = input ("dime la ciudad de andalucia y te diré el gentilicio: ")


EncuentraLaProvincia = False
i=0
while i <= 7 and not EncuentraLaProvincia:
    EncuentraLaProvincia = provincias [i] == respuesta
    i = i + 1
    
if EncuentraLaProvincia:
    print ("El gentilicio es: " + gentilicios [i-1])
else:
    print ("Inténtalo de nuevo o escribelo bien")
 