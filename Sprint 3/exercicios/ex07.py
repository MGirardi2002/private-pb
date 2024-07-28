a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def numero_impar(lista):
    nlista = []  
    for i in lista:
        if i % 2 != 0:
            nlista.append(i)
    return nlista
    
print(numero_impar(a)) 