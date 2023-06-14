pay = int(input('Сколько вы зарабатываете?'))
copl = int(input('Сколько вы хотите накопить?'))
c = 0
summ = 0
while summ != copl:
    c += 1
    summ += pay * 0,3
print('Вам придётся питаться дошиками ', c, ' день(-ня, -ней)')
