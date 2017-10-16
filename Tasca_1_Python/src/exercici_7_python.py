numero = input("Introdueix un número: ")

lista = list(numero)

listaReverse = [lista[i-1] for i in range(len(lista), 0, -1)]
if lista == listaReverse:
    print ("Es palíndrom")
else:
    print ("No es palíndrom")