from random import randint
warrior_1_hp = 100
warrior_2_hp = 100

while warrior_1_hp > 0 and warrior_2_hp > 0:
    if randint(1, 2) == 1:
        warrior_2_hp -= 20
        print('Воин 1 атакует! У воина 2 осталось', warrior_2_hp, 'очков здоровья')
    elif randint(1, 2) == 2:
        warrior_1_hp -= 20
        print('Воин 2 атакует! У воина 1 осталось', warrior_1_hp, 'очков здоровья')
if warrior_1_hp > warrior_2_hp:
    print('-' * 10)
    print('Воин 1 победил!')
elif warrior_2_hp > warrior_1_hp:
    print('-' * 10)
    print('Воин 2 победил!')