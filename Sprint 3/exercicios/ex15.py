class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
        
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada
        
lampada = Lampada(False)
lampada.liga()
print("A l�mpada est� ligada? ", lampada.esta_ligada())

lampada.desliga()
print("A l�mpada ainda est� ligada? ", lampada.esta_ligada()) 