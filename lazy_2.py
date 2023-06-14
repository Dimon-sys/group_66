import contextlib

my_file = open('test.txt', 'w')
my_file.write('Writing some info...')
my_file.close()

with open('test.txt', 'w') as my_file:
    my_file.write('Writing into file with context manager...')
    print(my_file.closed)

print(my_file.closed)

@contextlib.contextmanager
def str_reverse(my_str):
    print('Входим в контекстный менеджер:')
    yield my_str[::-1]
    print('Выходим из контекстного менеджера:')

with str_reverse('Hello, world!') as reversed_str:
    print(f'Выполняется код: {reversed_str}')


@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        print('Произошло исключение')

with exc_handler(IndexError):
    my_l = [1,2]
    print(my_l(3))

    