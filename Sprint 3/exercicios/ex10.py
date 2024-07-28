def remove_double(lista):
    return list(set(lista))
    
lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(remove_double(lista))