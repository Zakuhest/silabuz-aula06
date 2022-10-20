from easygui import *
import sys

""" Queremos asegurar un recinto presurizado. Establecemos un umbral de presión y un umbral de volumen: pThreshold = 2.3, vThreshold = 7.41. Se le pide que ingrese la presión y el volumen corriente del recinto y que escriba un guión que simula el siguiente comportamiento: 
– si el volumen y la presión están por encima de los umbrales: parada inmediata; 
– si solo la presión es superior al umbral de presión: solicite aumentar el volumen luz del altavoz; 
– si solo el volumen está por encima del volumen umbral: pida que disminuya el volumen del recinto; 
– si no declarar que “todo está bien”. """

# Hecho por CRISTIAN DIAZ

pThreshold = 2.3
vThreshold = 7.41
msg ="Asegurar un recinto presurizado"
title = "Ejercicio 1"
fieldNames = ["Presión","Volumen"]
fieldValues = []
val = True

msgbox(f"""
                  Umbral de presión    |    Umbral de volumen
                  pThreshold = {pThreshold}     |    vThreshold = {vThreshold}
    """)

while val:
    
    fieldValues = multenterbox(msg, title, fieldNames)

    while val:
        if fieldValues == None: sys.exit(0)
        errormsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":  # type: ignore
                errormsg = errormsg + (f"{fieldNames[i]} es un campo obligatorio.\n\n")
        if errormsg == "": break
        fieldValues = multenterbox(errormsg, title, fieldNames, fieldValues)
    # print("Presión:", fieldValues[0])
    # print("Volumen:", fieldValues[1])

    if float(fieldValues[0]) > pThreshold and float(fieldValues[1]) > vThreshold:  # type: ignore
        msgbox("Parado inmediato!", ok_button="Exit")
        sys.exit(0)
    elif float(fieldValues[0]) > pThreshold:  # type: ignore
        msgbox("Aumentar el volumen luz del altavoz", title="Advertencia!", ok_button="Continue")
        pass
    elif float(fieldValues[1]) > vThreshold:  # type: ignore
        msgbox("Disminuir el volumen del recinto", title="Advertencia!", ok_button="Continue")
        pass
    else:
        msgbox("Todo esta bien.", ok_button="Good job!")
        sys.exit(0)