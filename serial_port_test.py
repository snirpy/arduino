import serial
import serial.tools.list_ports


baud = 9600

print("Recherche d'un port serie...")

ports = serial.tools.list_ports.comports(include_links=False)

if (len(ports) != 0): # on a trouvé au moins un port actif

    if (len(ports) > 1):     # affichage du nombre de ports trouvés
        print (str(len(ports)) + " ports actifs ont ete trouves:") 
        ligne = 1
        for port in ports :  # affichage du nom de chaque port
            print(str(ligne) + ' : ' + port.device)
            ligne = ligne + 1
        portChoisi = int(input('Ecrivez le numero du port desire:'))
    else:
        print ("1 port actif a ete trouve:")
        portChoisi = 1

    # on établit la communication série
    arduino = serial.Serial(ports[portChoisi - 1].device, baud, timeout=1)
    # arduino = serial.Serial("COM4",timeout =1)
    print('Connexion a ' + arduino.name + ' a un baud rate de ' + str(baud))

    frequence = input("Frequence d'acquisition desiree, en Hz (max: 1000):  ")

    temps_pause = 1000.0/float(frequence)
    compteur = 0
    #on envoie à l'Arduino le message d'initialisation
    while True:
        compteur += 1
        arduino.write(b"i")

        arduino.write(b"e")
    
        donneesBrutes = str(arduino.readline())
        # print(str(compteur) + " : " + donneesBrutes[2:-5])
        print(str(compteur) + " : " + donneesBrutes[2:-4])
        # print(type(donneesBrutes))

else: # on n'a pas trouvé de port actif
    print("Aucun port actif n'a ete trouve")
