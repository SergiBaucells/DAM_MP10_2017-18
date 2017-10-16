def esApocaliptic(n): 

    n = str(2**num) 
    if '666' in n: 
        return True 
    else: 
        return False 


num = int(input('Introdueix un número:')) 
print(esApocaliptic(num)) 