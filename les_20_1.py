class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
s = Singleton()
print('Object created', s, id(s))
s1 = Singleton()
print('Object created', s1, id(s1))

def repair_deco(func):
    def wrapper(a, b):
        return func(a, b) - 1
    return wrapper

@repair_deco
def wrong_func(a, b):
    return a + b + 1

print(f'2 + 2 = {wrong_func(2, 2)}')
print(f'5 + 5 = {wrong_func(5, 5)}')