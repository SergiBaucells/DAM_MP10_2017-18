def comptador():

    while True:
        caracter = input("Introdueix una lletra: ")
        if(len(caracter)>1 or len(caracter)==0):
            print("Te que ser un caràcter i/o no pot estar buit!!!")
            caracter = "caracter"
            continue
        else:
            break

    while True:
        cadena = input("Introdueix una cadena: ")
        if (cadena == ""):
            print("La cadena no pot estar buida!!")
        else:
            comptador = 0
            for lletra in cadena:
                if lletra == caracter:
                    comptador = comptador + 1
            print("La lletra",caracter,"està",comptador,"vegades")
            break

print(comptador())
