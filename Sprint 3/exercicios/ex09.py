#Você deve Utilizar a função enumerate().

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice,(primeirosNome,sobreNome,idade) in enumerate(zip(primeirosNomes,sobreNomes,idades)):
    print(f"{indice} - {primeirosNome} {sobreNome} está com {idade} anos")