english_dict = {
    'яблоко' : 'apple',
    'молоко' : 'milk',
    'кот' : 'cat'
}
word = input('Введите слово на русском')
if word in english_dict:
    print(word + ' на английском языке будет ' + english_dict[word])
else:
    print('Такого слова нет в словаре')