def my_decorator(func_to_decorate):
    def decorated_func():
        print('Я начинаю работать')
        func_to_decorate()
        print('Я закончил работать')
    return decorated_func

@my_decorator
def my_func():
    print('Я работаю')
    
my_func()
