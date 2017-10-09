def calcula_qualificacio(puntuacio):
    if puntuacio > 1.0:
        resultat = "Ha de ser entre 0.0 i 1.0!!!"
    elif puntuacio >= 0.9:
        resultat = "Excel·lent"
    elif puntuacio >= 0.8:
        resultat = "Notable"
    elif puntuacio >= 0.7:
        resultat = "Bé"
    elif puntuacio >= 0.6:
        resultat = "Suficient"
    else:
        resultat = "Insuficient"
    return resultat


print("Introdueix un valor entre 0.0 i 1.0")
while True:
        puntuacio = float(input("Introdueix puntuació: "))
        print(calcula_qualificacio(puntuacio))