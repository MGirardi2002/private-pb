lista = ['ma�a', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in lista:
    if i == i[::-1]:
        print(f'A palavra: {i} � um pal�ndromo')
    else:
        print(f'A palavra: {i} n�o � um pal�ndromo')  