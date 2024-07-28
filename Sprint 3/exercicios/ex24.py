class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
         
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse = True)

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8, 1])

result_crescente = crescente.ordenacaoCrescente()
result_decrescente = decrescente.ordenacaoDecrescente()

print(result_crescente)
print(result_decrescente)