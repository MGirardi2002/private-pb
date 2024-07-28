import random

random_list = random.sample(range(500), 50)

sorted_list = sorted(random_list)
n = len(sorted_list)
if n%2 == 0:
    mediana = (sorted_list[n//2-1] + sorted_list[n//2]) / 2
else:
    mediana = sorted_list[n//2]

media = sum(random_list)/len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')