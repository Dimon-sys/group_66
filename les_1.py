def kalkulator(a, b, z):
    if z == '+':
        print('Сумма: ', a + b)
    elif znak == '-':
        print('Разность: ', a - b)
    elif znak == '*':
        print('Произведение: ', a * b)
    elif znak == '/':
        print('Частное: ', a / b)
    else:
        print('Операция не распознана')
number_1 = int(input())
number_2 = int(input())
znak = input()
file = open('result.txt', 'a')
file.write(kalkulator(number_1, number_2, znak))
file.close()