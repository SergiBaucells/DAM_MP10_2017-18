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
<<<<<<< HEAD
        
=======
        break
>>>>>>> d3ba0c6d933edd726efa5b0bc710bfa4482f7635
    except:
        print("Tenen que ser números!!!")
        
calcul_salari()
