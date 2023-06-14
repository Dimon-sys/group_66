#функция
def square(x):
    x_square = x * x
    print(f'{x} ^ 2 = {x_square}')
    return x_square

#процедура
def square_2(x):
    x_square = x * x
    print(f'{x} ^ 2 = {x_square}')

print(square(2))
print(square_2(2))