
def soma_num(string_numeros):
    numeros = string_numeros.split(',')
    
    soma = sum(int(numero) for numero in numeros)
    
    return soma
    
string_numeros = "1,3,4,6,10,76"
result = soma_num(string_numeros)
print(result)