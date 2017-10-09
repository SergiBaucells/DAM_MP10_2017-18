def num_xifres_sequencial(numero):
    return len(str(numero))
        

while True:
    try:
        numero = int(input("Introdueix un número: "))
        print("Número sequencial: " + str(num_xifres_sequencial(numero)))
        break
    except:
        print("El valor introduït ha de ser un número enter")

