# capitalize() retorna una copia de la cadena amb la primera lletra en majúscula
cadena = "python mola"
print(cadena.capitalize())

#center() retorna una copia de la cadena centrada
cadena = "python mola"
print(cadena.center(50," "))

#count() retorna la quantitat d'ocurrències de subcadenes
cadena = "python mola, python educa, python entreteneix!"
cadena2 = "python"
count = cadena.count(cadena2)
print(count)

#decode()+encode() descodifica/codifica la cadena utilitzant el còdec registrat per a la codificació
cadena = "python mola...!!!"
cadena = cadena.encode('UTF-8','strict')
print("String codificat: ", cadena)
print("String descodificat: ", cadena.decode('UTF-8','strict'))

#endswith() per saber si una cadena finalitza amb una subcadena determinada
cadena = "python mola"
print(cadena.endswith("mola"))
print(cadena.endswith("pyhton"))

#expandtabs() retorna una còpia de la cadena que tabula cuan troba "\t"
cadena = "python\tmola"
print(cadena.expandtabs(16))

#find() busca una subcadena dins d'una cadena
cadena = "python mola"
print(cadena.find("mola"))

#format() donar format a una cadena
cadena = "python mola {0}"
print(cadena.format(", mola molt!"))

#isalnum() per saber si una cadena es alfanumèrica
cadena = "pythonmola15"
print(cadena.isalnum())

#isalpha() per saber si una cadena es alfabètica
cadena = "pythonmola15"
print(cadena.isalpha())

#isdigit() per saber si una cadena es numèrica
cadena = "15"
print(cadena.isdigit())

#islower() per saber si una cadena conté domes minúscules
cadena = "python mola"
print(cadena.islower())

#isspace() per saber si una cadena conté domes espais en blanc
cadena = " "
print(cadena.isspace())

#istitle() per saber si una cadena es de format de títol
cadena = "python mola"
print(cadena.istitle())

#isupper() per saber si una cadena conté domes majúscules
cadena = "PYTHON MOLA"
print(cadena.isupper())

#ljust() per aliniar text a l'esquerra
cadena = "python mola"
print(cadena.ljust(20,"="))

#lower() converteix una cadena a minúscules
cadena = "PYTHON MOLA"
print(cadena.lower())

#lstrip() elimina caràcters a la esquerra d'una cadena
cadena = "www.pythonmola.com"
print(cadena.lstrip("w."))

#partition() parteix una cadena en 3 parts, utilitzant un separador
cadena = "http://www.pythonmola.com".partition("www.")
print(cadena)

#replace() substitueix text a una cadena
cadena = "nom"
cadena2 = "Sergi"
print("Hola nom".replace(cadena,cadena2))

#split() converteix una cadena de text en un array de cadenes de text
cadena = "python mola"
print(cadena.split())

#splitlines() partir una cadena en línies
cadena = "python\nmola\nmolt"
print(cadena.splitlines())

#startswith() per saber si una cadena comença amb una subcadena
cadena = "python mola"
print(cadena.startswith("python"))

#strip() elimina caràcters a l'esquerra i dreta d'una cadena
cadena = "   python mola   "
print(cadena.strip(" "))

#swapcase() converteix majúscules a minúscules i al revés
cadena = "python MOLA"
print(cadena.swapcase())

#title() converteix una cadena a format títol
cadena = "python mola"
print(cadena.title())

#translate() retorna una copia de la cadena ambs els caràcters asignats a través d'una taula de
#            traducció assignada

#upper() converteix una cadena a majúscules
cadena = "python mola"
print(cadena.upper())

#zfill() retorna un text anteposant zeros
cadena = "1515"
print(cadena.zfill(10))