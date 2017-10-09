def calcul_salari():
    try:
        hores = int(input("Introdueix hores: "))
        tarifa = float(input("Introdueix tarifa: "))
        if hores > 40:
            hores_extra = hores - 40
            hores = hores - hores_extra
            hores_extra = hores_extra*1.5
        hores = hores + hores_extra
        print("Salari: " + str(round(tarifa*hores,2)))
        
    except:
        print("Tenen que ser números!!!")
        
calcul_salari()
