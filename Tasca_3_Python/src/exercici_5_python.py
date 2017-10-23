cad = 'X-DSPAM-Confidence: 0.8475 Km'
cad1 = cad.find(str(":"))+1
cad2 = cad.find(str("Km"))-1
print(float(cad[cad1:cad2]))
