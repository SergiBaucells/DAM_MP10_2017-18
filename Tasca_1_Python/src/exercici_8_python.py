def num_primer():
    a = 0
    numero = int(input("Introdueix un número: "))
    for i in range(1, numero + 1):
        if(numero % i == 0):
            a = a + 1
    if(a != 2):
        print("No es primer")
    else:
        print("Es primer")

num_primer()