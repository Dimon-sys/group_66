try:
    input_var_1 = int(input('Введите число 1 '))
    input_var_2 = int(input('Введите число 2 '))

except ValueError:
    print('Вы ввели неправильные значения')
else:
    result = input_var_1 + input_var_2
    print(result)

    if input_var_1 > input_var_2:
        print(input_var_1, ' больше ', input_var_2)
    elif input_var_1 < input_var_2:
        print(input_var_1, ' меньше ', input_var_2)
    else:
        print(input_var_1, ' равно ', input_var_2)