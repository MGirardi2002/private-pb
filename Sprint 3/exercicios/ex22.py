class Pessoa:
    def __init__(self, id):
        self.__nome = None
        self.id = id
    
    # getter
    def nome(self):
        return self.__nome
       
    # setter    
    def nome(self,valor):
        self.__nome = valor
        
pessoa = Pessoa(1)
pessoa.nome = 'Fulano de Tal'
print(pessoa.nome)