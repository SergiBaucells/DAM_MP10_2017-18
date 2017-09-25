#booleà = True # Declaracio de variables amb accents acceptat
#print(type (booleà)) # Veure tipus de dades
#print("Rodríguez") # Els accents són acceptats
#
### PEMDSR = Parèntesis-elevació-multiplicació-divisió-suma-resta
#print ((5 + 2) ** (2 * 4)) 
#print (5 + 2 ** 2 * 4)
#print (5 + 2 // 2 * 4)
#
#
###Demanar informació a l'usuari'
#nom = input('¿Com et dius?\n')
#edat = input('¿Quina edat tens?\n') 
#print("El teu nom és: " + nom)
### Mètode str, converteix el contingut a un String després d'haver-lo pasat a int
#print("La teva edat és: " + edat + " \nEl doble de la teva edat és: " + str (int(edat) * 2))

## ifelse
#if True :
#    print('Cert')
#    print('2ª línia')
#else :
#    print('Fals')
#
#if False :
#    print('Cert')
#    print('2ª línia')
#else :
#    print('Fals')
#    print('Més fals')
#
#num=1
#if False :
#    print('Cert')
#    print('2ª línia')
#elif num>=1: # sino, si
#    print('Fals')
#    print('Més fals')
#else:
#    print ('Més cert')
    
## Try/Except
#while True:
#    try:
#        numero = input("Introdueix un número: ")
#        print(int(numero) + 2)
#    except:
#        print("T'havia demanat un número!!!")

## Bucle While
#edad = 0
#while edad < 18:
#    edad = edad + 1
#    if edad == 15:
#        continue # El que hi ha a continuació no s'executarà, tornarà al principi del while
#    print ("Felicidades, tienes " + str(edad))

