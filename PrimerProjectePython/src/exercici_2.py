while True:
    try:
        hores = int(input("Introdueix hores: "))
        tarifa = float(input("Introdueix tarifa: "))
        print("Salari: " + str(round(tarifa*hores,2)))
        break
    except:
        print("Tenen que ser números!!!")