def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
        
    for key,value in kwargs.items():
        print(value)
        
my_function(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)