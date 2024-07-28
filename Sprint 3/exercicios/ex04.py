def primo(n):
    if n <= 1:
        return False
        
    for i in range(2,int(n **0.5)+1):
        if n % i == 0:
            return False
    
    return True
    
def count_primos(limit):
    for num in range(limit + 1):
        if primo(num):
            print(num)
    
limit = 100
count_primos(limit)