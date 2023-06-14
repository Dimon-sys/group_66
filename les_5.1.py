films_dict = {
    'Начало' : 'Леонардо Ди Каприо',
    'Миссия невыполнима' : 'Том Круз'
}
favourite_actor = 'Леонардо Ди Каприо'
film = input('Какой фильм вы собираетесь посмотреть?')
if film in films_dict:
    actor = films_dict.get(film)
    if actor == favourite_actor:
        print('Этот фильм стоит просмотра')
    else:
        print('Не стоит это смотреть')