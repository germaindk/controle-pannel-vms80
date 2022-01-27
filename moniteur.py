import serial
import serial.tools.list_ports

print("Recherche d'un port serie...")

ports = serial.tools.list_ports.comports(include_links=False)

if (len(ports) != 0): # on a trouvé au moins un port actif

    if (len(ports) > 1):     # affichage du nombre de ports trouvés
        print (str(len(ports)) + " ports actifs ont ete trouves:") 
    else:
        print ("1 port actif a ete trouve:")

    ligne = 1

    for port in ports :  # affichage du nom de chaque port
        print(str(ligne) + ' : ' + port.device)
        ligne = ligne + 1