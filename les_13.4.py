def calculate():
    print('Укажите интересующие вас операции')
    print('* - умножение')
    print('+ - сложение')
    print('- - вычитание')
    print('/ - деление')

    operation = input()

    if operation == '*':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) * int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '/':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) / int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '+':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) + int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '-':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) - int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    else:
        print('Операция неизвестна')

        
    calculate()

calculate()