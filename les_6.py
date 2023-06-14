questions = [
    {'question': 'Кто сыграл 10-го Доктора?',
    'answers': ['Дэвид Теннант', 'Мэтт Смит', 'Джуди Уиттакер'],
    'right': 1},

    {'question': 'Кто является культовым антагонистом Доктора?',
    'answers': ['Киберлюди', 'Мастер', 'Джек Хадсон'],
    'right': 2},

    {'question': 'В каком году состоялся перезапуск Доктора Кто?',
    'answers': [2000, 2008, 2005],
    'right': 3},

    {'question': 'Да?',
    'answers': ['Да', 'Возможно', 'Нет'],
    'right': 1},
]

name = input('Введите своё имя: ')
c = 0
for question in questions:
    print(question.get('question'))
    answer_number = 0
    for answer in question['answers'] :
        answer_number += 1
        print(answer_number, '.', answer)
    user_answer = int(input('Ваш ответ: '))
    if user_answer == question.get('right'):
        print('Верно')
        c += 1
    else:
        print('Неверно')
    print('-' * 20)
print('Верных ответов: ', c)

file = open('result.txt', 'a')
file.write('Игрок', name, 'набрал', c, 'очков.\n')
file.close()