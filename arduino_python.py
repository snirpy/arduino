import serial
import os
import time

import serial.tools.list_ports
def mesure():
    rawdata =[]
    compt = 0

    try:
        arduino = serial.Serial("/dev/cu.usbmodem1401",timeout =1)
    except:
        print("\nVérifier si le port est déja utilisé par une communication série")
        print("Fin de communication\n")
    else:

        while True:
            rawdata.append(str(arduino.readline()))
            compt += 1
            # time.sleep(10)
            
            
            for element in rawdata:
                print(element[2:-5])
                # print(element)
                print("")
mesure()
