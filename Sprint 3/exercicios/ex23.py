class Calculo:
    def __init__(self):
        pass
        
    def soma(self, x, y):
        resultado = x+y
        return f'Somando: {x} + {y} = {resultado}'
        
        
    def sub(self, x, y):
        resultado = x-y
        return f'Subtraindo: {x} - {y} = {resultado}'

x=4
y=5
calc = Calculo()
result_sum = calc.soma(x,y)
result_sub = calc.sub(x,y)
print(result_sum)
print(result_sub)