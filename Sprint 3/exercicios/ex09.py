#Voc� deve Utilizar a fun��o enumerate().

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'Jos�']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice,(primeirosNome,sobreNome,idade) in enumerate(zip(primeirosNomes,sobreNomes,idades)):
    print(f"{indice} - {primeirosNome} {sobreNome} est� com {idade} anos")