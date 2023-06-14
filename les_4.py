import random
a = random.randint(1, 10)
b = int(input('Введите число от 1 до 10'))
if b == a:
    print("Поздравляю, вы угадали!")
elif b != a:
    if a - b <= 1 or b - a <= 1:
        print('Почти получилось')
    else:
        print('Вы проиграли. Сочувствую')