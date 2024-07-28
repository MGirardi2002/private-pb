def function(lista):
    size_sublists = len(lista) // 3
    
    lista1 = lista[:size_sublists]
    lista2 = lista[size_sublists:2*size_sublists]
    lista3 = lista[2*size_sublists:]
    
    return [lista1,lista2,lista3]
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista1,lista2,lista3 = function(lista)
print(lista1,lista2,lista3)