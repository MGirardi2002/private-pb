class Aviao:
    cor = "azul"
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        
        
aviao1 = Aviao("BOIENG", 1500, 400)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)

avioes = [aviao1,aviao2,aviao3]

for aviao in avioes:
    print(f"O avião de modelo \"{aviao.modelo}\" possui uma velocidade máxima de {aviao.velocidade_maxima} km/h; capacidade para {aviao.capacidade} passageiros e é da cor \"{aviao.cor}\"")