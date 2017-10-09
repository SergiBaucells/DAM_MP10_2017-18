def num_xifres_iteratiu(numero):
    comptador = 1
    
    while (numero > 10):
        numero = numero / 10
        comptador = comptador + 1
    return comptador        

while True:
    try:
        numero = int(input("Introdueix un número: "))
        print("Número iteratiu: " + str(num_xifres_iteratiu(numero)))
        break
    except:
        print("El valor introduït ha de ser un número enter")

