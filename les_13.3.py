def add(a, b):
    return a + b

print(add(1, 23))

def hello():
    name = input('Как вас зовут? ')
    print('Привет, ' + name)
    hello()

hello()