provincias = ["Almeria","Sevilla", "Cordoba", "Cadiz", "Granada", "Malaga", "Huelva", "Jaen"]
gentilicios = ["Almeriense","Sevillano", "Cordobee", "Pisha", "Granaino", "Malagueño", "Onubense", "Jienense"]

respuesta = input ("Dime la ciudad y te diré el gentilicio: ")
i=0
EncuentraLaProvincia = False

while i <= 7 and not EncuentraLaProvincia:
    EncuentraLaProvincia = provincias [i] == respuesta
    i = i + 1
if EncuentraLaProvincia:
    print ("El gentilicio es: " + gentilicios [i-1])
else:
    print ("Inténtalo de nuevo o escribelo bien")
 