class Passaro:
    def __init__(self, som):
        self.som = som
    
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        print(self.som)

class Pato(Passaro):
    def __init__(self):
        super().__init__("Quack Quack")
        
    def mostrar(self):
        print("Pato")
        self.voar()
        print("Pato emitindo som...")
        self.emitir_som()
        
class Pardal(Passaro):
    def __init__(self):
        super().__init__("Piu Piu")
    
    def mostrar(self):
        print("Pardal")
        self.voar()
        print("Pardal emitindo som...")
        self.emitir_som()
        

pato = Pato()
pardal = Pardal()

pato.mostrar()
print()
pardal.mostrar()
